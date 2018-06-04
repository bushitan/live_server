# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0012_mgrimage_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgrtag',
            name='show_mobile',
            field=models.IntegerField(default=1, verbose_name='\u662f\u5426\u79fb\u52a8\u7aef\u663e\u793a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')]),
        ),
    ]
