# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_remove_message_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='player_url',
            new_name='player',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='pusher_url',
            new_name='pusher',
        ),
    ]
