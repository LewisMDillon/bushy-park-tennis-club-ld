# Generated by Django 3.2.20 on 2023-08-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0004_auto_20230809_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='reservation_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='reservation_time',
            new_name='time',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='title',
            field=models.CharField(default='Court Reservation', max_length=200),
        ),
    ]
