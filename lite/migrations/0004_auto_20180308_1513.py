# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0003_auto_20180308_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelibrary',
            name='local_path',
            field=models.ImageField(default=b'', upload_to=b'static/img/', verbose_name='\u56fe\u6807'),
        ),
    ]
