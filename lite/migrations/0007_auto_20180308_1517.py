# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0006_auto_20180308_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelibrary',
            name='local_path',
            field=models.ImageField(upload_to=b'static/img/', null=True, verbose_name='\u56fe\u6807', blank=True),
        ),
    ]
