# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0027_remove_users_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='pppp',
            field=models.CharField(default=b'otha', max_length=20),
        ),
    ]
