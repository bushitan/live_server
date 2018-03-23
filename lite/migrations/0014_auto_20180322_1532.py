# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0013_auto_20180320_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('app', models.ForeignKey(verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', blank=True, to='lite.App', null=True)),
            ],
            options={
                'verbose_name': '\u56fe\u5e93\u6807\u7b7e',
                'verbose_name_plural': '\u56fe\u5e93\u6807\u7b7e',
            },
        ),
        migrations.RemoveField(
            model_name='filelibrary',
            name='user',
        ),
        migrations.AddField(
            model_name='filelibrary',
            name='app',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', blank=True, to='lite.App', null=True),
        ),
        migrations.AddField(
            model_name='filelibrary',
            name='file_tag',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u6807\u7b7e', blank=True, to='lite.FileTag', null=True),
        ),
    ]
