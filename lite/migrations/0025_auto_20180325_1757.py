# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0024_remove_user_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_teacher',
            field=models.IntegerField(default=0, verbose_name='\u662f\u5426\u8bb2\u5e08', choices=[(0, '\u542c\u4f17'), (1, '\u8bb2\u5e08')]),
        ),
    ]
