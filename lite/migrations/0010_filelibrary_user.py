# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0009_app_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='filelibrary',
            name='user',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u7528\u6237', blank=True, to='lite.User', null=True),
        ),
    ]
