# Generated by Django 3.2.20 on 2023-08-22 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20230821_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
