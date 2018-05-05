# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0029_user_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='latitude',
            field=models.FloatField(default=0, verbose_name='\u7eac\u5ea6'),
        ),
        migrations.AlterField(
            model_name='company',
            name='longitude',
            field=models.FloatField(default=0, verbose_name='\u7cbe\u5ea6'),
        ),
    ]
