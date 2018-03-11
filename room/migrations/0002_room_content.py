# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0008_auto_20180308_1527'),
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='content',
            field=models.ForeignKey(related_name='room_content', verbose_name='\u5185\u5bb9\u56fe\u7247', blank=True, to='lite.FileLibrary', null=True),
        ),
    ]
