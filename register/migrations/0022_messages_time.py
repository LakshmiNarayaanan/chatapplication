# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0021_remove_messages_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='time',
            field=models.CharField(default=0.0, max_length=20),
        ),
    ]