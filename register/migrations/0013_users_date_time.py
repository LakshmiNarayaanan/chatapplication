# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20181128_0800'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='date_time',
            field=models.DateTimeField(default=0),
        ),
    ]
