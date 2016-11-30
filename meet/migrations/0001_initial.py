# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('elevation', models.FloatField(null=True)),
                ('hacc', models.FloatField(null=True)),
                ('vacc', models.FloatField(null=True)),
                ('sensor', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=64, null=True, blank=True)),
                ('entity', models.CharField(default=b'EC', max_length=50)),
                ('unit', models.CharField(default=b'\xc2\xb5S/cm', max_length=20)),
                ('value', models.FloatField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
