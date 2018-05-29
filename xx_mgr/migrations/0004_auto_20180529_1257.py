# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0003_auto_20180529_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mgrtag',
            name='lx_item',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u7559\u5b66\u5b50\u680f\u76ee', choices=[(0, '\u4e13\u4e1a\u89e3\u6790'), (1, '\u7559\u5b66\u3001\u79fb\u6c11\u65b9\u6848'), (2, '\u9662\u6821\u5217\u8868'), (3, '\u7533\u8bf7\u65f6\u95f4\u89c4\u5212\u8868'), (4, '\u7533\u8bf7\u653b\u7565')]),
        ),
    ]
