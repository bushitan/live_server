# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True),
        ),
    ]
