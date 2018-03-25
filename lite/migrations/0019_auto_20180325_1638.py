# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0018_auto_20180323_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='filelibrary',
            name='is_alive',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u6709\u6548', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b')]),
        ),
        migrations.AddField(
            model_name='filelibrary',
            name='is_show',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u663e\u793a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')]),
        ),
        migrations.AddField(
            model_name='filelibrary',
            name='is_top',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u6307\u5b9a', choices=[(0, '\u4e0d\u7f6e\u9876'), (1, '\u7f6e\u9876')]),
        ),
        migrations.AddField(
            model_name='filelibrary',
            name='issue_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='filelibrary',
            name='name_admin',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u79f0', blank=True),
        ),
        migrations.AddField(
            model_name='filelibrary',
            name='serial',
            field=models.IntegerField(default=0, verbose_name='\u6392\u5e8f'),
        ),
        migrations.AddField(
            model_name='filetag',
            name='is_alive',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u6709\u6548', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b')]),
        ),
        migrations.AddField(
            model_name='filetag',
            name='is_show',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u663e\u793a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')]),
        ),
        migrations.AddField(
            model_name='filetag',
            name='is_top',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u6307\u5b9a', choices=[(0, '\u4e0d\u7f6e\u9876'), (1, '\u7f6e\u9876')]),
        ),
        migrations.AddField(
            model_name='filetag',
            name='issue_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='filetag',
            name='name_admin',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u79f0', blank=True),
        ),
        migrations.AddField(
            model_name='filetag',
            name='serial',
            field=models.IntegerField(default=0, verbose_name='\u6392\u5e8f'),
        ),
        migrations.AlterField(
            model_name='filelibrary',
            name='app',
            field=models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App'),
        ),
        migrations.AlterField(
            model_name='filelibrary',
            name='name',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5c0f\u7a0b\u5e8f\u663e\u793a\u540d\u79f0', blank=True),
        ),
        migrations.AlterField(
            model_name='filetag',
            name='app',
            field=models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App'),
        ),
        migrations.AlterField(
            model_name='filetag',
            name='name',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5c0f\u7a0b\u5e8f\u663e\u793a\u540d\u79f0', blank=True),
        ),
    ]
