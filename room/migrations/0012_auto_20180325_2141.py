# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0011_auto_20180325_1730'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='im_num',
        ),
        migrations.RemoveField(
            model_name='room',
            name='player',
        ),
        migrations.RemoveField(
            model_name='room',
            name='pusher',
        ),
    ]
