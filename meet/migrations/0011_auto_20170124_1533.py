# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0010_meetpunt_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetpunt',
            name='thumbnail',
            field=models.ImageField(max_length=200, null=True, upload_to=b'thumbnails/', blank=True),
        ),
    ]
