# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0013_auto_20180325_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-create_time'], 'verbose_name': '\u5c01\u9762\u5927\u56fe', 'verbose_name_plural': '\u5c01\u9762\u5927\u56fe'},
        ),
    ]
