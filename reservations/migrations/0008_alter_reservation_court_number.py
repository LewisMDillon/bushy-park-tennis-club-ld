# Generated by Django 3.2.20 on 2023-08-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_reservation_timeslot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='court_number',
            field=models.IntegerField(choices=[(0, 'Court 1'), (1, 'Court 2'), (2, 'Court 3'), (3, 'Court 4'), (4, 'Court 5'), (5, 'Court 6'), (6, 'Court 7'), (7, 'Court 8'), (8, 'Court 9')]),
        ),
    ]