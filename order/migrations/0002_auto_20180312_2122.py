# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cost',
            options={'ordering': ['-create_time'], 'verbose_name': '\u8d39\u7528\u660e\u7ec6', 'verbose_name_plural': '\u8d39\u7528\u660e\u7ec6'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['-create_time'], 'verbose_name': '\u4f1a\u5458\u5217\u8868', 'verbose_name_plural': '\u4f1a\u5458\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-create_time'], 'verbose_name': '\u652f\u4ed8\u8ba2\u5355', 'verbose_name_plural': '\u652f\u4ed8\u8ba2\u5355'},
        ),
        migrations.AddField(
            model_name='cost',
            name='duration',
            field=models.IntegerField(default=0, verbose_name='\u4f1a\u5458\u6301\u7eed\u65f6\u95f4'),
        ),
    ]
