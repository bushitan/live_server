# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0005_auto_20180324_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_alive',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u6709\u6548', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b')]),
        ),
        migrations.AddField(
            model_name='news',
            name='is_show',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u663e\u793a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')]),
        ),
        migrations.AddField(
            model_name='news',
            name='name_admin',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5c0f\u7a0b\u5e8f\u663e\u793a\u540d\u79f0', blank=True),
        ),
    ]
