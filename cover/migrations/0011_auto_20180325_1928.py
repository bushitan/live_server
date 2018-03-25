# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0010_auto_20180325_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='room',
            field=models.ForeignKey(related_name='rrr', verbose_name='\u76f4\u64ad\u623f\u95f4', blank=True, to='room.Room', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='\u6807\u9898'),
        ),
    ]
