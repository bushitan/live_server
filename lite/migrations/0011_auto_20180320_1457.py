# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0010_filelibrary_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelibrary',
            name='style',
            field=models.IntegerField(default=1, verbose_name='\u7c7b\u522b', choices=[(1, '\u97f3\u9891'), (2, '\u89c6\u9891')]),
        ),
    ]
