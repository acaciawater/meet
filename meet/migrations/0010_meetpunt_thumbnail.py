# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0009_auto_20170111_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetpunt',
            name='thumbnail',
            field=models.ImageField(max_length=200, null=True, upload_to=b'thumbnails', blank=True),
        ),
    ]
