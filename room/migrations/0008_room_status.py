# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0007_auto_20180320_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='status',
            field=models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u51c6\u5907'), (1, '\u8fdb\u884c\u4e2d'), (2, '\u5df2\u7ecf\u8f93')]),
        ),
    ]
