# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo', models.CharField(default=b'', max_length=300, null=True, verbose_name='logo\u94fe\u63a5', blank=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('nick_name', models.CharField(max_length=100, null=True, verbose_name='\u5fae\u4fe1\u6635\u79f0', blank=True)),
                ('wx_id', models.CharField(max_length=100, null=True, verbose_name='\u5fae\u4fe1\u53f7', blank=True)),
                ('wx_open_id', models.CharField(max_length=50, null=True, verbose_name='\u5fae\u4fe1OpenID', blank=True)),
                ('wx_session_key', models.CharField(max_length=128, null=True, verbose_name='\u5fae\u4fe1SessionKey', blank=True)),
                ('wx_expires_in', models.FloatField(null=True, verbose_name='\u5fae\u4fe1SessionKey\u8fc7\u671f\u65f6\u95f4', blank=True)),
                ('session', models.CharField(max_length=128, null=True, verbose_name='Django\u7684session', blank=True)),
                ('expires', models.FloatField(null=True, verbose_name='Django\u7684session\u8fc7\u671f\u65f6\u95f4', blank=True)),
                ('uuid', models.CharField(max_length=32, null=True, verbose_name='uuid\u6807\u8bc6', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True)),
                ('phone', models.CharField(max_length=40, null=True, verbose_name='\u624b\u673a', blank=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237_\u57fa\u672c\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237_\u57fa\u672c\u4fe1\u606f',
            },
        ),
    ]
