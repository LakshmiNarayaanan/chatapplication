# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-06 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20181105_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name=b'c_password',
        ),
        migrations.AddField(
            model_name='login',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='login',
            name='email',
            field=models.EmailField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='login',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
