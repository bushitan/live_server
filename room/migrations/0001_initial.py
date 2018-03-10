# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('style', models.IntegerField(default=0, verbose_name='\u7c7b\u578b', choices=[(0, '\u6587\u5b57'), (1, '\u56fe\u7247'), (2, '\u8bed\u97f3')])),
                ('text', models.CharField(max_length=400, null=True, verbose_name='\u6587\u5b57', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True)),
                ('audio', models.ForeignKey(verbose_name='\u8bed\u97f3', blank=True, to='lite.FileLibrary', null=True)),
                ('image', models.ForeignKey(related_name='message_image', verbose_name='\u56fe\u7247', blank=True, to='lite.FileLibrary', null=True)),
            ],
            options={
                'verbose_name': '\u5b98\u65b9\u4fe1\u606f',
                'verbose_name_plural': '\u5b98\u65b9\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('im_num', models.CharField(max_length=100, null=True, verbose_name='IM\u623f\u95f4\u53f7', blank=True)),
                ('pusher', models.CharField(max_length=500, null=True, verbose_name='\u63a8\u6d41\u5730\u5740', blank=True)),
                ('player', models.CharField(max_length=500, null=True, verbose_name='\u64ad\u653e\u5730\u5740', blank=True)),
                ('style', models.IntegerField(default=0, verbose_name='\u623f\u95f4\u7c7b\u578b', choices=[(0, '\u51c6\u5907'), (1, '\u76f4\u64ad'), (2, '\u7eaf\u6587\u5b57')])),
                ('title', models.CharField(max_length=100, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('description', models.CharField(max_length=100, null=True, verbose_name='\u63cf\u8ff0', blank=True)),
                ('serial', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('is_show', models.IntegerField(default=1, verbose_name='\u662f\u5426\u663e\u793a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True)),
                ('app', models.ForeignKey(verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', blank=True, to='lite.App', null=True)),
                ('cover', models.ForeignKey(related_name='room_cover', verbose_name='\u4e3b\u9898\u5c01\u9762', blank=True, to='lite.FileLibrary', null=True)),
            ],
            options={
                'ordering': ['-serial'],
                'verbose_name': '\u804a\u5929\u5ba4',
                'verbose_name_plural': '\u804a\u5929\u5ba4',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u804a\u5929\u5ba4', blank=True, to='room.Room', null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='user',
            field=models.ForeignKey(verbose_name='\u7528\u6237', blank=True, to='lite.User', null=True),
        ),
    ]
