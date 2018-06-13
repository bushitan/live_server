# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0013_mgrtag_show_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgrtag',
            name='logo',
            field=models.ForeignKey(verbose_name='\u624b\u673a\u56fe\u6807', blank=True, to='xx_mgr.MGRImage', null=True),
        ),
    ]
