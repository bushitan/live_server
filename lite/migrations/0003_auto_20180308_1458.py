# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0002_auto_20180308_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='app',
            options={'verbose_name': 'APP\u5e94\u7528', 'verbose_name_plural': 'APP\u5e94\u7528'},
        ),
        migrations.AlterField(
            model_name='filelibrary',
            name='local_path',
            field=models.ImageField(upload_to=b'static/img/', null=True, verbose_name='\u56fe\u6807', blank=True),
        ),
    ]
