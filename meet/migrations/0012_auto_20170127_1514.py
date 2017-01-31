# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0011_auto_20170124_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetpunt',
            name='thumbnail',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/thumbnails/', location=b'thumbnails/'), max_length=200, null=True, upload_to=b'thumbnails/', blank=True),
        ),
    ]
