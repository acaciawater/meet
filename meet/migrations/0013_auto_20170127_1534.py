# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import meet.util


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0012_auto_20170127_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetpunt',
            name='thumbnail',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/thumbnails/', location=b'thumbnails/'), max_length=200, null=True, upload_to=meet.util.thumbnail_upload, blank=True),
        ),
    ]
