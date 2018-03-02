# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0001_initial'),
    ]

    operations = [
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
    ]
