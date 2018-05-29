# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0002_auto_20180529_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mgrarticle',
            name='address',
        ),
        migrations.RemoveField(
            model_name='mgrarticle',
            name='audio_author',
        ),
        migrations.RemoveField(
            model_name='mgrarticle',
            name='audio_name',
        ),
        migrations.RemoveField(
            model_name='mgrarticle',
            name='audio_poster',
        ),
        migrations.RemoveField(
            model_name='mgrarticle',
            name='audio_src',
        ),
        migrations.RemoveField(
            model_name='mgrarticle',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='mgrarticle',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='mgrarticle',
            name='video_src',
        ),
        migrations.RemoveField(
            model_name='mgrarticle',
            name='work_date',
        ),
        migrations.AddField(
            model_name='mgrtag',
            name='lx_item',
            field=models.IntegerField(default=0, verbose_name='\u6240\u5c5e\u7f51\u7ad9', choices=[(0, '\u4e13\u4e1a\u89e3\u6790'), (1, '\u7559\u5b66\u3001\u79fb\u6c11\u65b9\u6848'), (2, '\u9662\u6821\u5217\u8868'), (3, '\u7533\u8bf7\u65f6\u95f4\u89c4\u5212\u8868'), (4, '\u7533\u8bf7\u653b\u7565')]),
        ),
    ]
