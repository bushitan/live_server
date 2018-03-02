# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0004_auto_20180302_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='issue_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u5e03\u65f6\u95f4'),
        ),
    ]
