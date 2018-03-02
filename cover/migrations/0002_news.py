# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True)),
                ('title', models.CharField(max_length=100, null=True, verbose_name='\u6807\u9898', blank=True)),
                ('summary', models.CharField(max_length=100, null=True, verbose_name='\u6458\u8981', blank=True)),
                ('des', models.CharField(max_length=100, null=True, verbose_name='\u8be6\u7ec6\u63cf\u8ff0', blank=True)),
                ('footer', models.CharField(max_length=100, null=True, verbose_name='\u9875\u811a', blank=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('article', models.ForeignKey(verbose_name='\u70b9\u51fb\u6587\u7ae0', blank=True, to='cover.ArticleLibrary', null=True)),
                ('cover_image', models.ForeignKey(verbose_name='\u5c01\u9762\u56fe\u7247', blank=True, to='cover.ImageLibrary', null=True)),
            ],
            options={
                'ordering': ['-create_time'],
                'verbose_name': '6.1 \u76ee\u5f55 -- \u65b0\u95fb',
                'verbose_name_plural': '6.1 \u76ee\u5f55 -- \u65b0\u95fb',
            },
        ),
    ]
