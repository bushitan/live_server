# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0011_auto_20180320_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatarUrl',
            field=models.CharField(max_length=100, null=True, verbose_name='\u5934\u50cf', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=100, null=True, verbose_name='\u56fd\u5bb6', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(max_length=100, null=True, verbose_name='\u57ce\u5e02', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6027\u522b', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='province',
            field=models.CharField(max_length=100, null=True, verbose_name='\u4f4d\u7f6e', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nick_name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u6635\u79f0', blank=True),
        ),
    ]
