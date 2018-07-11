# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speak', '0002_auto_20180711_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakuser',
            name='theme',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u9898\u76ee', blank=True, to='speak.SpeakTheme', null=True),
        ),
        migrations.AlterField(
            model_name='speaktheme',
            name='voice',
            field=models.ForeignKey(related_name='speak_teacher_voice', verbose_name='\u8001\u5e08\u793a\u8303\u5f55\u97f3', blank=True, to='lite.FileLibrary', null=True),
        ),
    ]
