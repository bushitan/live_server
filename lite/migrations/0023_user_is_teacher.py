# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0022_auto_20180325_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_teacher',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u8bb2\u5e08', choices=[(0, '\u542c\u4f17'), (1, '\u8bb2\u5e08')]),
        ),
    ]
