# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meet', '0002_meting_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meting',
            name='user',
        ),
    ]
