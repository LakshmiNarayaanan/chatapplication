# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-28 11:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0024_auto_20181128_1058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='users',
            name='date_time',
        ),
    ]