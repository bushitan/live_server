# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0011_mgrkeyword_key_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgrimage',
            name='style',
            field=models.IntegerField(default=0, verbose_name='\u56fe\u7247\u7c7b\u578b', choices=[(0, '\u4e0a\u4f20'), (1, '\u57fa\u7840')]),
        ),
    ]
