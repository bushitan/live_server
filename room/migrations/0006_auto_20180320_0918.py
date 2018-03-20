# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_message_is_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True),
        ),
        migrations.AddField(
            model_name='room',
            name='name_admin',
            field=models.CharField(max_length=100, null=True, verbose_name='admin\u540e\u53f0\u540d\u79f0', blank=True),
        ),
    ]
