# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvp', '0007_stage_background_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stage',
            name='orientation',
            field=models.IntegerField(default=0, verbose_name='\u65b9\u5411', choices=[(0, '\u7ad6\u5c4f'), (1, '\u6a2a\u5c4f')]),
        ),
        migrations.AlterField(
            model_name='stagefile',
            name='style',
            field=models.IntegerField(default=0, verbose_name='\u7c7b\u522b', choices=[(0, '\u56fe\u7247'), (1, '\u97f3\u9891'), (2, '\u89c6\u9891')]),
        ),
    ]
