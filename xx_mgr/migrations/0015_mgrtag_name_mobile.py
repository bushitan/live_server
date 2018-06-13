# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0014_mgrtag_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgrtag',
            name='name_mobile',
            field=models.CharField(default=b'', max_length=100, null=True, verbose_name='\u624b\u673a\u663e\u793a\u540d\u79f0', blank=True),
        ),
    ]
