# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvp', '0002_auto_20180326_0934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='background',
            name='style',
        ),
    ]
