# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0008_auto_20180308_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u540d\u79f0', blank=True),
        ),
    ]
