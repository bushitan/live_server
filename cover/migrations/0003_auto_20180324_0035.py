# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0002_auto_20180322_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='app',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App'),
        ),
    ]
