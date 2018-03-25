# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0023_user_is_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='logo',
        ),
    ]
