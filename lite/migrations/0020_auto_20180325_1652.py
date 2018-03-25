# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0019_auto_20180325_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='app',
            field=models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App'),
        ),
        migrations.AddField(
            model_name='company',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='company',
            name='is_alive',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u6709\u6548', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b')]),
        ),
        migrations.AddField(
            model_name='company',
            name='is_show',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u663e\u793a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')]),
        ),
        migrations.AddField(
            model_name='company',
            name='is_top',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u6307\u5b9a', choices=[(0, '\u4e0d\u7f6e\u9876'), (1, '\u7f6e\u9876')]),
        ),
        migrations.AddField(
            model_name='company',
            name='issue_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='company',
            name='name_admin',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u79f0', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='serial',
            field=models.IntegerField(default=0, verbose_name='\u6392\u5e8f'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5c0f\u7a0b\u5e8f\u663e\u793a\u540d\u79f0', blank=True),
        ),
    ]
