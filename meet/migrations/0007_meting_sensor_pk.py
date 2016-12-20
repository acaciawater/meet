# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0006_auto_20161215_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='meting',
            name='sensor_pk',
            field=models.ForeignKey(default=1, to='meet.Sensor'),
            preserve_default=False,
        ),
    ]
