# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import meet.util


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0013_auto_20170127_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetpunt',
            name='thumbnail',
            field=models.ImageField(max_length=200, null=True, upload_to=meet.util.thumbnail_upload, blank=True),
        ),
    ]
