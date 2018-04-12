# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0014_auto_20180411_0914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='is_teacher',
        ),
    ]
