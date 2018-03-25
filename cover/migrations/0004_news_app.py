# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0018_auto_20180323_1653'),
        ('cover', '0003_auto_20180324_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='app',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', blank=True, to='lite.App', null=True),
        ),
    ]
