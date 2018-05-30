# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0030_auto_20180423_1121'),
        ('xx_mgr', '0007_auto_20180530_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='MGRImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5c0f\u7a0b\u5e8f\u663e\u793a\u540d\u79f0', blank=True)),
                ('name_admin', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u79f0', blank=True)),
                ('is_top', models.IntegerField(default=1, verbose_name='\u662f\u5426\u6307\u5b9a', choices=[(0, '\u4e0d\u7f6e\u9876'), (1, '\u7f6e\u9876')])),
                ('is_show', models.IntegerField(default=1, verbose_name='\u662f\u5426\u663e\u793a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_alive', models.IntegerField(default=1, verbose_name='\u662f\u5426\u6709\u6548', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b')])),
                ('serial', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('issue_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('url', models.CharField(max_length=1000, null=True, verbose_name='\u4e91\u5730\u5740', blank=True)),
                ('local_path', models.ImageField(default=b'', upload_to=b'static/img/', null=True, verbose_name='\u56fe\u6807', blank=True)),
                ('app', models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App')),
            ],
            options={
                'verbose_name': '\u56fe\u5e93',
                'verbose_name_plural': '\u56fe\u5e93',
            },
        ),
    ]
