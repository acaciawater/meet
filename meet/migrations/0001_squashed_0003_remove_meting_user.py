# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'meet', '0001_initial'), (b'meet', '0002_meting_user'), (b'meet', '0003_remove_meting_user')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
