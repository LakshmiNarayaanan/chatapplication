# Generated by Django 2.1.3 on 2018-11-05 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='age',
        ),
        migrations.RemoveField(
            model_name='login',
            name='gender',
        ),
    ]
