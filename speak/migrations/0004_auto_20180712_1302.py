# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speak', '0003_auto_20180711_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speaktheme',
            name='content',
            field=models.TextField(default=b'', null=True, verbose_name='\u5185\u5bb9', blank=True),
        ),
    ]
