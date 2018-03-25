# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0021_auto_20180325_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_url',
            field=models.CharField(max_length=500, null=True, verbose_name='\u5934\u50cf', blank=True),
        ),
    ]
