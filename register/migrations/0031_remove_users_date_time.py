# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0030_auto_20181128_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='date_time',
        ),
    ]
