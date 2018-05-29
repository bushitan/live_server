# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0030_auto_20180423_1121'),
    ]

    operations = [
        migrations.CreateModel(
            name='MGRArticle',
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
                ('click_rate', models.IntegerField(default=8965, verbose_name='\u70b9\u51fb\u7387')),
                ('style', models.IntegerField(default=1, verbose_name='\u6587\u7ae0\u7c7b\u522b', choices=[(1, b'\xe6\x99\xae\xe9\x80\x9a'), (2, b'\xe7\xba\xaf\xe6\x96\x87\xe5\xad\x97'), (3, b'\xe9\x9f\xb3\xe9\xa2\x91'), (4, b'\xe8\xa7\x86\xe9\xa2\x91'), (5, b'\xe7\x9b\xb4\xe6\x92\xad\xe5\x9b\x9e\xe6\x94\xbe')])),
                ('title', models.CharField(max_length=100, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('subtitle', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5b50\u6807\u9898', blank=True)),
                ('summary', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u6458\u8981', blank=True)),
                ('source', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u6765\u6e90', blank=True)),
                ('content', models.TextField(null=True, verbose_name='\u6b63\u6587', blank=True)),
                ('content_width', models.IntegerField(default=750, null=True, verbose_name='\u6b63\u6587\u663e\u793a\u5bbd\u5ea6', blank=True)),
                ('audio_src', models.CharField(max_length=1000, null=True, verbose_name='\u97f3\u9891\u5730\u5740(Url)', blank=True)),
                ('audio_poster', models.CharField(max_length=500, null=True, verbose_name='\u97f3\u9891\u5c01\u9762\u56fe(Url)', blank=True)),
                ('audio_name', models.CharField(max_length=100, null=True, verbose_name='\u97f3\u9891\u540d\u79f0', blank=True)),
                ('audio_author', models.CharField(max_length=100, null=True, verbose_name='\u97f3\u9891\u4f5c\u8005', blank=True)),
                ('video_src', models.CharField(max_length=1000, null=True, verbose_name='\u89c6\u9891\u5730\u5740(Url)', blank=True)),
                ('address', models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5730\u5740', blank=True)),
                ('work_date', models.CharField(default=b'', max_length=200, null=True, verbose_name='\u5de5\u4f5c\u65f6\u95f4', blank=True)),
                ('phone', models.CharField(default=b'', max_length=40, null=True, verbose_name='\u7535\u8bdd', blank=True)),
                ('introduction', models.CharField(default=b'', max_length=500, null=True, verbose_name='\u7b80\u4ecb', blank=True)),
                ('app', models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App')),
            ],
            options={
                'ordering': ['-issue_time', '-is_top'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='MGRTag',
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
                ('web_site', models.IntegerField(default=0, verbose_name='\u6240\u5c5e\u7f51\u7ad9', choices=[(0, '\u7559\u5b66'), (1, '\u79fb\u6c11')])),
                ('app', models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App')),
                ('father', models.ForeignKey(verbose_name='\u7236\u7c7b\u680f\u76ee', blank=True, to='xx_mgr.MGRTag', null=True)),
            ],
            options={
                'ordering': ['-serial'],
                'verbose_name': '\u680f\u76ee',
                'verbose_name_plural': '\u680f\u76ee',
            },
        ),
        migrations.AddField(
            model_name='mgrarticle',
            name='tag',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u680f\u76ee', blank=True, to='xx_mgr.MGRTag', null=True),
        ),
    ]
