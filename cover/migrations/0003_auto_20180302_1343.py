# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cover', '0002_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlelibrary',
            options={'ordering': ['-issue_time', '-is_top'], 'verbose_name': '\u6587\u7ae0', 'verbose_name_plural': '\u6587\u7ae0'},
        ),
        migrations.AlterModelOptions(
            name='imagelibrary',
            options={'verbose_name': '\u56fe\u5e93', 'verbose_name_plural': '\u56fe\u5e93'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-create_time'], 'verbose_name': '\u4e13\u680f', 'verbose_name_plural': '\u4e13\u680f'},
        ),
        migrations.AddField(
            model_name='news',
            name='tag',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u6807\u7b7e', blank=True, to='cover.Tag', null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='article',
            field=models.ForeignKey(verbose_name='\u94fe\u63a5\u6587\u7ae0', blank=True, to='cover.ArticleLibrary', null=True),
        ),
    ]
