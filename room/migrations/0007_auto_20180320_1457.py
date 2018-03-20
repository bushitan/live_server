# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0006_auto_20180320_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='audio',
            field=models.CharField(default=b'', max_length=500, null=True, verbose_name='\u8bed\u97f3', blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.CharField(default=b'', max_length=500, null=True, verbose_name='\u56fe\u7247', blank=True),
        ),
    ]
