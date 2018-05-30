# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0006_auto_20180529_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mgrtag',
            name='web_site',
            field=models.IntegerField(default=0, verbose_name='\u6240\u5c5e\u7f51\u7ad9', choices=[(0, '\u7559\u5b66'), (1, '\u79fb\u6c11'), (2, '\u516c\u5171')]),
        ),
    ]
