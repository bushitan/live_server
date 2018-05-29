# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xx_mgr', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mgrarticle',
            options={'ordering': ['-issue_time'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
    ]
