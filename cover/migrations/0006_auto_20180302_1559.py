# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0005_news_issue_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagelibrary',
            name='local_path',
            field=models.ImageField(upload_to=b'static/img/', verbose_name='\u56fe\u6807'),
        ),
    ]
