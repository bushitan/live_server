# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0003_auto_20180302_1343'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleLibrary',
            new_name='Article',
        ),
    ]
