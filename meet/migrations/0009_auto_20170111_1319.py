# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import meet.util


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0008_auto_20170105_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetpunt',
            name='end',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='meetpunt',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='meetpunt',
            name='start',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='meetpunt',
            name='thumbnail',
            field=models.ImageField(max_length=200, null=True, upload_to='thumbnails', blank=True),
        ),
    ]
