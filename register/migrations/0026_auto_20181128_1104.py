# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0025_auto_20181128_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='date_time',
            field=models.DateTimeField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='date_time',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterField(
            model_name='messages',
            name='time',
            field=models.CharField(default=b'0.0', max_length=20),
        ),
    ]
