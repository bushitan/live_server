# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0013_auto_20180320_1534'),
        ('room', '0008_room_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pusheruser',
            name='room',
        ),
        migrations.AddField(
            model_name='pusheruser',
            name='app',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', blank=True, to='lite.App', null=True),
        ),
    ]
