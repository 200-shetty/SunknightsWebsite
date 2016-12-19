# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-19 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunknightsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordrole',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discordrole',
            name='discord_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
