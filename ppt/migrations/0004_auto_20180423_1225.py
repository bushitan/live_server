# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0030_auto_20180423_1121'),
        ('ppt', '0003_auto_20180423_1128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pptteam',
            options={'ordering': ['-serial'], 'verbose_name': '\u56e2\u961f', 'verbose_name_plural': '\u56e2\u961f'},
        ),
        migrations.AlterModelOptions(
            name='pptteamuser',
            options={'ordering': ['-serial'], 'verbose_name': '\u6210\u5458', 'verbose_name_plural': '\u6210\u5458'},
        ),
        migrations.AddField(
            model_name='pptfile',
            name='upload_user',
            field=models.ForeignKey(related_name='upload_user', verbose_name='\u4e0a\u4f20\u8005', blank=True, to='lite.User', null=True),
        ),
    ]
