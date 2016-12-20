# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from tastypie.models import create_api_key
from django.template.loader import render_to_string
from django.core.validators import RegexValidator
PostalCodeValidator = RegexValidator(regex=r'^\d{4}\s*[A-Z]{2}$', message="Ongeldige postcode")
SENSOR_TYPES = (
     ('EC', 'Sodaq EC Meter'),
     ('N', 'Nitraat Meter'),
     )
 
# auto create api keys
models.signals.post_save.connect(create_api_key, sender=User)

class Sensor(models.Model):
    user = models.ForeignKey(User)
    sensor_id = models.CharField(max_length=50,unique=True)
    sensor_type = models.CharField(max_length=16,choices=SENSOR_TYPES,default='EC')
    assigned = models.DateTimeField()

class UserProfileData(models.Model):
    user = models.OneToOneField(User)
    street = models.CharField(max_length=255,null=True,default='')
    number = models.PositiveIntegerField()
    postalcode = models.CharField(max_length=16,null=True,default='',validators=[PostalCodeValidator])
    city = models.CharField(max_length=255,null=True,default='')
    state = models.CharField(max_length=255,null=True,default='')
    country = models.CharField(max_length=255,default='NL')

class Meting(models.Model):
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
    class Meta:
        verbose_name_plural = 'metingen'
        
    
