# Generated by Django 3.2.20 on 2023-08-22 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]
