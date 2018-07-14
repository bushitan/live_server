# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0030_auto_20180423_1121'),
        ('speak', '0004_auto_20180712_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakBonus',
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
                ('action', models.IntegerField(blank=True, null=True, verbose_name='\u64cd\u4f5c', choices=[(0, '\u6253\u5361'), (1, '\u5206\u4eab'), (2, '\u6d88\u8d39')])),
                ('app', models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App')),
                ('theme', models.ForeignKey(verbose_name='\u6240\u5c5e\u9898\u76ee', blank=True, to='speak.SpeakTheme', null=True)),
                ('user_other', models.ForeignKey(related_name='bonus_other', verbose_name='\u5bf9\u65b9', blank=True, to='lite.User', null=True)),
                ('user_self', models.ForeignKey(related_name='bonus_self', verbose_name='\u81ea\u5df1', blank=True, to='lite.User', null=True)),
            ],
            options={
                'ordering': ['-serial'],
                'verbose_name': '\u7528\u6237\u79ef\u5206',
                'verbose_name_plural': '\u7528\u6237\u79ef\u5206',
            },
        ),
    ]
