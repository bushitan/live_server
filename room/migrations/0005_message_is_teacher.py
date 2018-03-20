# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0004_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_teacher',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u8bb2\u5e08\u53d1\u8a00', choices=[(0, '\u542c\u4f17'), (1, '\u8bb2\u5e08')]),
        ),
    ]
