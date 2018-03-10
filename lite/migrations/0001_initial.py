# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_id', models.CharField(max_length=100, null=True, verbose_name='AppID', blank=True)),
                ('secret_key', models.CharField(max_length=100, null=True, verbose_name='SecretKey', blank=True)),
                ('longitude', models.CharField(max_length=32, null=True, verbose_name='\u7ecf\u5ea6', blank=True)),
                ('latitude', models.CharField(max_length=32, null=True, verbose_name='\u7eac\u5ea6', blank=True)),
                ('taste_qr', models.CharField(max_length=500, null=True, verbose_name='\u4f53\u9a8c\u4e8c\u7ef4\u7801', blank=True)),
            ],
            options={
                'verbose_name': '\u673a\u6784\u5c55\u793a\u4fe1\u606f',
                'verbose_name_plural': '\u673a\u6784\u5c55\u793a\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('phone', models.CharField(max_length=40, null=True, verbose_name='\u624b\u673a', blank=True)),
                ('introduction', models.CharField(default=b'', max_length=500, null=True, verbose_name='\u4e2a\u4eba\u7b80\u4ecb', blank=True)),
                ('address', models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('latitude', models.FloatField(default=0, verbose_name='\u7cbe\u5ea6')),
                ('longitude', models.FloatField(default=0, verbose_name='\u7ef4\u5ea6')),
            ],
            options={
                'verbose_name': '\u673a\u6784\u5c55\u793a\u4fe1\u606f',
                'verbose_name_plural': '\u673a\u6784\u5c55\u793a\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='FileLibrary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('url', models.CharField(max_length=1000, null=True, verbose_name='\u4e91\u5730\u5740', blank=True)),
                ('style', models.IntegerField(default=1, verbose_name='\u7c7b\u522b', choices=[(1, '\u5c01\u9762'), (2, '\u5934\u50cf')])),
                ('local_path', models.ImageField(upload_to=b'static/img/', verbose_name='\u56fe\u6807')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u56fe\u5e93',
                'verbose_name_plural': '\u56fe\u5e93',
            },
        ),
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
                ('app', models.ForeignKey(verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', blank=True, to='lite.App', null=True)),
            ],
            options={
                'verbose_name': '\u7528\u6237_\u57fa\u672c\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237_\u57fa\u672c\u4fe1\u606f',
            },
        ),
    ]
