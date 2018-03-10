# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='app',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='app',
            name='taste_qr',
        ),
    ]
