# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from tastypie.models import create_api_key
from django.template.loader import render_to_string

# auto create api keys
models.signals.post_save.connect(create_api_key, sender=User)

class Meting(models.Model):
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
        
    class Meta:
        verbose_name_plural = 'metingen'
        
