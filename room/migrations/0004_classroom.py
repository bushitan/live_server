# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0010_filelibrary_user'),
        ('room', '0003_pusheruser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_pusher', models.CharField(max_length=100, null=True, verbose_name='\u6559\u5ba4\u63a8\u6d41\u5730\u5740', blank=True)),
                ('teacher_player', models.CharField(max_length=100, null=True, verbose_name='\u6559\u5ba4\u64ad\u653e\u5730\u5740', blank=True)),
                ('student_pusher', models.CharField(max_length=100, null=True, verbose_name='\u5b66\u751f\u63a8\u6d41\u5730\u5740', blank=True)),
                ('student_player', models.CharField(max_length=100, null=True, verbose_name='\u5b66\u751f\u64ad\u653e\u5730\u5740', blank=True)),
                ('key', models.CharField(max_length=32, null=True, verbose_name='\u79d8\u94a5', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True)),
                ('app', models.ForeignKey(verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', blank=True, to='lite.App', null=True)),
                ('teacher', models.ForeignKey(verbose_name='\u8001\u5e08', blank=True, to='lite.User', null=True)),
            ],
            options={
                'verbose_name': '1v1\u6559\u5ba4',
                'verbose_name_plural': '1v1\u6559\u5ba4',
            },
        ),
    ]
