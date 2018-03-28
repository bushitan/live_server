# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lite', '0027_auto_20180326_0931'),
        ('pvp', '0003_remove_background_style'),
    ]

    operations = [
        migrations.CreateModel(
            name='StageFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5c0f\u7a0b\u5e8f\u663e\u793a\u540d\u79f0', blank=True)),
                ('name_admin', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u79f0', blank=True)),
                ('is_top', models.IntegerField(default=1, verbose_name='\u662f\u5426\u6307\u5b9a', choices=[(0, '\u4e0d\u7f6e\u9876'), (1, '\u7f6e\u9876')])),
                ('is_show', models.IntegerField(default=1, verbose_name='\u662f\u5426\u663e\u793a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_alive', models.IntegerField(default=1, verbose_name='\u662f\u5426\u6709\u6548', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b')])),
                ('serial', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('issue_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('url', models.CharField(max_length=1000, null=True, verbose_name='\u4e91\u5730\u5740', blank=True)),
                ('style', models.IntegerField(default=1, verbose_name='\u7c7b\u522b', choices=[(1, '\u97f3\u9891'), (2, '\u89c6\u9891')])),
                ('local_path', models.ImageField(default=b'', upload_to=b'static/img/', null=True, verbose_name='\u56fe\u6807', blank=True)),
                ('app', models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App')),
            ],
            options={
                'verbose_name': '\u56fe\u5e93',
                'verbose_name_plural': '\u56fe\u5e93',
            },
        ),
        migrations.CreateModel(
            name='StageTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u5c0f\u7a0b\u5e8f\u663e\u793a\u540d\u79f0', blank=True)),
                ('name_admin', models.CharField(default=b'', max_length=100, null=True, verbose_name='\u540e\u53f0\u663e\u793a\u540d\u79f0', blank=True)),
                ('is_top', models.IntegerField(default=1, verbose_name='\u662f\u5426\u6307\u5b9a', choices=[(0, '\u4e0d\u7f6e\u9876'), (1, '\u7f6e\u9876')])),
                ('is_show', models.IntegerField(default=1, verbose_name='\u662f\u5426\u663e\u793a', choices=[(0, '\u9690\u85cf'), (1, '\u663e\u793a')])),
                ('is_alive', models.IntegerField(default=1, verbose_name='\u662f\u5426\u6709\u6548', choices=[(0, '\u5931\u6548'), (1, '\u6fc0\u6d3b')])),
                ('serial', models.IntegerField(default=0, verbose_name='\u6392\u5e8f')),
                ('issue_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('description', models.CharField(max_length=100, null=True, verbose_name='\u7b80\u4ecb', blank=True)),
                ('app', models.ForeignKey(default=1, verbose_name='\u6240\u5c5e\u5c0f\u7a0b\u5e8f', to='lite.App')),
            ],
            options={
                'ordering': ['-serial'],
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.RemoveField(
            model_name='stage',
            name='background',
        ),
        migrations.RemoveField(
            model_name='stage',
            name='config',
        ),
        migrations.AddField(
            model_name='stage',
            name='height',
            field=models.CharField(max_length=20, null=True, verbose_name='\u9ad8\u5ea6', blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='player_height',
            field=models.CharField(max_length=20, null=True, verbose_name='\u64ad\u653e\u9ad8\u5ea6', blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='player_width',
            field=models.CharField(max_length=20, null=True, verbose_name='\u64ad\u653e\u5bbd\u5ea6', blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='player_x',
            field=models.CharField(max_length=20, null=True, verbose_name='\u64ad\u653ex', blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='player_y',
            field=models.CharField(max_length=20, null=True, verbose_name='\u64ad\u653ey', blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='pusher_height',
            field=models.CharField(max_length=20, null=True, verbose_name='\u5f55\u5236\u9ad8\u5ea6', blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='pusher_width',
            field=models.CharField(max_length=20, null=True, verbose_name='\u5f55\u5236\u5bbd\u5ea6', blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='pusher_x',
            field=models.CharField(max_length=20, null=True, verbose_name='\u5f55\u5236x', blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='pusher_y',
            field=models.CharField(max_length=20, null=True, verbose_name='\u5f55\u5236y', blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='width',
            field=models.CharField(max_length=20, null=True, verbose_name='\u5bbd\u5ea6', blank=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='audio_image',
            field=models.ForeignKey(related_name='audio_image', verbose_name='\u80cc\u666f\u97f3\u4e50', blank=True, to='pvp.StageFile', null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='background_image',
            field=models.ForeignKey(related_name='background_image', verbose_name='\u80cc\u666f\u56fe\u7247', blank=True, to='pvp.StageFile', null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='cover_image',
            field=models.ForeignKey(related_name='cover_image', verbose_name='\u5c01\u9762\u56fe\u7247', blank=True, to='pvp.StageFile', null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='player_image',
            field=models.ForeignKey(related_name='player_image', verbose_name='\u64ad\u653e\u906e\u76d6\u56fe\u7247', blank=True, to='pvp.StageFile', null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='pusher_image',
            field=models.ForeignKey(related_name='pusher_image', verbose_name='\u5f55\u5236\u906e\u76d6\u56fe\u7247', blank=True, to='pvp.StageFile', null=True),
        ),
        migrations.AddField(
            model_name='stage',
            name='tag',
            field=models.ForeignKey(verbose_name='\u6240\u5c5e\u6807\u7b7e', blank=True, to='pvp.StageTag', null=True),
        ),
    ]
