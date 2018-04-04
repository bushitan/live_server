# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pvp', '0006_pvpmember'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='background_audio',
            field=models.ForeignKey(related_name='background_audio', verbose_name='\u80cc\u666f\u97f3\u4e50', blank=True, to='pvp.StageFile', null=True),
        ),
    ]
