# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0008_mgrimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='mgrarticle',
            name='cover',
            field=models.ForeignKey(verbose_name='\u5c01\u9762', blank=True, to='xx_mgr.MGRImage', null=True),
        ),
    ]
