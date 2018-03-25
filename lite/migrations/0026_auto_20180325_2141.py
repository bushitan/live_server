# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0025_auto_20180325_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='im_num',
            field=models.CharField(max_length=100, null=True, verbose_name='IM\u623f\u95f4\u53f7', blank=True),
        ),
        migrations.AddField(
            model_name='app',
            name='player',
            field=models.CharField(max_length=500, null=True, verbose_name='\u64ad\u653e\u5730\u5740', blank=True),
        ),
        migrations.AddField(
            model_name='app',
            name='pusher',
            field=models.CharField(max_length=500, null=True, verbose_name='\u63a8\u6d41\u5730\u5740', blank=True),
        ),
    ]
