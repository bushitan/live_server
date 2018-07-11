# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0030_auto_20180423_1121'),
        ('speak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaktheme',
            name='voice',
            field=models.ForeignKey(related_name='speak_teacher_voice', verbose_name='\u8001\u5e08\u793a\u8303', blank=True, to='lite.FileLibrary', null=True),
        ),
        migrations.AlterField(
            model_name='speakuser',
            name='voice',
            field=models.ForeignKey(related_name='speak_user_voice', verbose_name='\u5f55\u97f3', blank=True, to='lite.FileLibrary', null=True),
        ),
    ]
