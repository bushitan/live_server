# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0030_auto_20180423_1121'),
        ('ppt', '0002_pptteam_pptteamuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='pptfile',
            name='tag',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u6807\u7b7e', blank=True, to='ppt.PPTTag', null=True),
        ),
        migrations.AddField(
            model_name='ppttag',
            name='team',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u56e2\u961f', blank=True, to='ppt.PPTTeam', null=True),
        ),
        migrations.AddField(
            model_name='ppttag',
            name='user',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237', blank=True, to='lite.User', null=True),
        ),
        migrations.AlterField(
            model_name='pptteamuser',
            name='team',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u56e2\u961f', blank=True, to='ppt.PPTTeam', null=True),
        ),
    ]
