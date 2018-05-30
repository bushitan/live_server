# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0010_mgrkeyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgrkeyword',
            name='key_word',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5173\u952e\u5b57\u540d\u79f0', blank=True),
        ),
    ]
