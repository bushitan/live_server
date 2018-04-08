# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0027_auto_20180326_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filelibrary',
            name='style',
            field=models.IntegerField(default=0, verbose_name='\u7c7b\u522b', choices=[(0, '\u56fe\u7247'), (1, '\u97f3\u9891'), (2, '\u89c6\u9891')]),
        ),
    ]
