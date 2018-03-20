# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0012_auto_20180320_1507'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avatarUrl',
            new_name='avatar_url',
        ),
    ]
