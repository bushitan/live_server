# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0004_auto_20180529_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mgrtag',
            name='lx_item',
        ),
        migrations.AddField(
            model_name='mgrarticle',
            name='lx_item',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u7559\u5b66\u5b50\u680f\u76ee', choices=[(0, '\u4e13\u4e1a\u89e3\u6790'), (1, '\u7559\u5b66\u3001\u79fb\u6c11\u65b9\u6848'), (2, '\u9662\u6821\u5217\u8868'), (3, '\u7533\u8bf7\u65f6\u95f4\u89c4\u5212\u8868'), (4, '\u7533\u8bf7\u653b\u7565')]),
        ),
        migrations.AddField(
            model_name='mgrarticle',
            name='lx_know',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u7559\u5b66\u6211\u60f3\u4e86\u89e3', choices=[(0, '\u7559\u5b66\u65b0\u95fb'), (1, '\u9662\u6821\u8d44\u8baf'), (2, '\u4e13\u4e1a\u63a8\u4ecb'), (3, '\u7b7e\u8bc1\u6307\u5357'), (4, '\u9662\u6821\u6392\u540d'), (5, '\u884c\u524d\u51c6\u5907'), (6, '\u7559\u5b66\u89c4\u5212'), (7, '\u7559\u5b66\u767e\u95ee'), (8, '\u6d77\u5916\u5956\u5b66\u91d1'), (9, '\u7559\u5b66\u62a5\u544a'), (10, '\u5907\u8003\u8d44\u8baf')]),
        ),
    ]
