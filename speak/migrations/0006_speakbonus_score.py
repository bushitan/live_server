# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speak', '0005_speakbonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakbonus',
            name='score',
            field=models.IntegerField(null=True, verbose_name='\u5206\u6570', blank=True),
        ),
    ]
