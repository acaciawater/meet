# -*- coding: utf-8 -*-
'''
@author: stephane
'''

import util, logging, os
import pandas as pd
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from tastypie.models import create_api_key
from django.template.loader import render_to_string
from django.core.validators import RegexValidator
from django.conf import settings
from django.core.files.storage import FileSystemStorage

PostalCodeValidator = RegexValidator(regex=r'^\d{4}\s*[A-Z]{2}$', message="Ongeldige postcode")
SENSOR_TYPES = (
     ('EC', 'Sodaq EC Meter'),
     ('N', 'Nitraat Meter'),
     )
 
# auto create api keys
models.signals.post_save.connect(create_api_key, sender=User)


class Meetpunt(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=200, null=True)
    end = models.DateTimeField(null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to=util.thumbnail_upload,
                                  max_length=200, blank=True, null=True)
    
    def __str__(self):
        return str(self.id)
    
    def assignStartEnd(self):
        metingen = self.meting_set.all()
        if metingen.count() == 0:
            # log cant assign start end, no meetpunt
            pass
        if metingen.count() == 1:
            datum = metingen[0].date
            self.end = datum
            self.start = datum
        else:
            m = self.meting_set.order_by('date', 'pk')
            self.start = m[0].date
            self.end = m[len(m)-1].date

    def to_pandas(self):
        metingen = self.meting_set.all()
        dates = [meting.date for meting in metingen]
        values = [meting.value for meting in metingen]
        return pd.Series(values,index=dates,name=self.name).sort_index()
    
    def make_thumbnail(self):
#         logger = self.getLogger()
#         logger.debug('Generating thumbnail for series %s' % self.name)
        try:
            if self.meting_set.all().count() != 0:
                series = self.to_pandas()
                dest =  slugify(unicode(self.name))+'.png'
                self.thumbnail.name = dest
                imagefile = os.path.join(settings.MEDIA_ROOT, 'thumbnails', dest)
                imagedir = os.path.dirname(imagefile)
                if not os.path.exists(imagedir):
                    os.makedirs(imagedir)
                util.save_thumbnail(series, imagefile)
#             logger.debug('Generated thumbnail %s' % dest)

        except Exception as e:
#             logger.exception('Error generating thumbnail: %s' % e)
            pass
        return self.thumbnail

class Sensor(models.Model):
    user = models.ForeignKey(User)
    sensor_id = models.CharField(max_length=50,unique=True)
    sensor_type = models.CharField(max_length=16,choices=SENSOR_TYPES,default='EC')
    assigned = models.DateTimeField()

    def __str__(self):
        return self.sensor_id

class UserProfileData(models.Model):
    user = models.OneToOneField(User)
    street = models.CharField(max_length=255,null=True,default='')
    number = models.PositiveIntegerField()
    postalcode = models.CharField(max_length=16,null=True,default='',validators=[PostalCodeValidator])
    city = models.CharField(max_length=255,null=True,default='')
    state = models.CharField(max_length=255,null=True,default='')
    country = models.CharField(max_length=255,default='NL')

class Meting(models.Model):
    meetpunt = models.ForeignKey(Meetpunt,null=True,blank=True)
    sensor_pk = models.ForeignKey(Sensor)
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation = models.FloatField(null=True)
    hacc = models.FloatField(null=True)
    vacc = models.FloatField(null=True)
    sensor = models.CharField(max_length=64)
    phone = models.CharField(max_length=64,null=True,blank=True)
    entity = models.CharField(max_length=50,default='EC')
    unit = models.CharField(max_length=20, default='µS/cm')
    value = models.FloatField()
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.pk)

    def as_html(self):
        return render_to_string('meting.html',context={'meting':self})
        
    def to_dict(self):
        result = {'latitude' : self.latitude, 
                  'longitude' : self.longitude,
                  'elevation' : self.elevation,
                  'hacc' : self.hacc,
                  'vacc' : self.vacc,
                  'sensor' : self.sensor,
                  'phone' : self.phone,
                  'entity' : self.entity,
                  'unit' : self.unit,
                  'value' : self.value,
                  'date' : self.date}
        return result


    def assignMeetpunt(self):
        meetpunt = self.findMeetpunt() 
        if meetpunt:
            self.meetpunt_id = meetpunt
        return meetpunt
        
    def findMeetpunt(self):
#         logger = logging.getLogger(__name__)
        if self.hacc > 25:
#             logger.debug('Cannot assign meting %s to a meetpunt, horizontal accuracy (%d) is too high' %(self, self.hacc))
            return None
        else:
            within_range = []
            for mp in Meetpunt.objects.all():
                if util.is_in_range(self, mp, 25):
                    within_range.append(mp)
        if len(within_range)== 0:
            mp = Meetpunt()
            mp.latitude = self.latitude
            mp.longitude = self.longitude
            mp.save()
            return mp
#              log mp created and assigned
        elif len(within_range)== 1:
            return within_range[0]
        else:
            closest = None
            for mp in within_range:
                if closest == None:
                    closest = mp
                else:
                    if util.distance(self, mp) < util.distance(self, closest):
                        closest = mp
            return closest                
             
    
    class Meta:
        verbose_name_plural = 'metingen'
    
def assignMetingPostSave(sender, instance, *args, **kwargs):
    ''' assigns meetpunt to meting and updates start/end for meetpunt '''
    meetpunt = instance.assignMeetpunt()
    models.signals.post_save.disconnect(assignMetingPostSave, sender=Meting)
    instance.save()
    models.signals.post_save.connect(assignMetingPostSave, sender=Meting)
    meetpunt.assignStartEnd()
    meetpunt.save()

models.signals.post_save.connect(assignMetingPostSave, sender=Meting)

