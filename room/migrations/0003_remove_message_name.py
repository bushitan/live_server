# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0002_auto_20180307_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='name',
        ),
    ]
