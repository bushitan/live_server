# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0028_auto_20180408_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=100, null=True, verbose_name='\u59d3\u540d', blank=True),
        ),
    ]
