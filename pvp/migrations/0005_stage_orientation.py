# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvp', '0004_auto_20180328_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='orientation',
            field=models.IntegerField(default=0, verbose_name='\u65b9\u5411', choices=[(0, '\u6c34\u5e73'), (1, '\u7ad6\u76f4')]),
        ),
    ]
