# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0027_auto_20180326_0931'),
        ('pvp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
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
                ('style', models.IntegerField(default=1, verbose_name='\u7c7b\u522b', choices=[(1, '\u97f3\u9891'), (2, '\u89c6\u9891')])),
                ('local_path', models.ImageField(default=b'', upload_to=b'static/img/', null=True, verbose_name='\u56fe\u6807', blank=True)),
                ('app', models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App')),
                ('user', models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237', blank=True, to='lite.User', null=True)),
            ],
            options={
                'verbose_name': '\u80cc\u666f',
                'verbose_name_plural': '\u80cc\u666f',
            },
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='app',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='user',
        ),
        migrations.AlterField(
            model_name='stage',
            name='background',
            field=models.ForeignKey(verbose_name='\u80cc\u666f\u56fe\u7247', blank=True, to='pvp.Background', null=True),
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]
