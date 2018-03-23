# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lite', '0017_auto_20180323_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='app',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='app',
            name='sys_user',
            field=models.OneToOneField(related_name='system_user', null=True, blank=True, to=settings.AUTH_USER_MODEL, verbose_name='\u7cfb\u7edf\u7ba1\u7406\u5458'),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
