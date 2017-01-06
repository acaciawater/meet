# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0007_meting_sensor_pk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meetpunt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='meting',
            name='meetpunt',
            field=models.ForeignKey(blank=True, to='meet.Meetpunt', null=True),
        ),
    ]
