# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0012_auto_20180325_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='app',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='teacher',
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': '\u7559\u8a00', 'verbose_name_plural': '\u7559\u8a00'},
        ),
        migrations.DeleteModel(
            name='Classroom',
        ),
    ]
