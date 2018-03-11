# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0009_app_name'),
        ('room', '0002_room_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='PusherUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='\u521b\u5efa\u65f6\u95f4', blank=True)),
                ('room', models.ForeignKey(verbose_name='\u6240\u5c5e\u804a\u5929\u5ba4', blank=True, to='room.Room', null=True)),
                ('user', models.ForeignKey(verbose_name='\u7528\u6237', blank=True, to='lite.User', null=True)),
            ],
            options={
                'verbose_name': '\u63a8\u6d41\u7528\u6237',
                'verbose_name_plural': '\u63a8\u6d41\u7528\u6237',
            },
        ),
    ]
