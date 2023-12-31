from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Reservation(models.Model):
    TIMESLOTS = [
        (0, '09:00'),
        (1, '10:00'),
        (2, '11:00'),
        (3, '12:00'),
        (4, '13:00'),
        (5, '14:00'),
        (6, '15:00'),
        (7, '16:00'),
        (8, '17:00'),
        (9, '18:00'),
        (10, '19:00'),
        (11, '20:00'),
    ]

    COURTS = [
        (0, 'Court 1'),
        (1, 'Court 2'),
        (2, 'Court 3'),
        (3, 'Court 4'),
        (4, 'Court 5'),
        (5, 'Court 6'),
        (6, 'Court 7'),
        (7, 'Court 8'),
        (8, 'Court 9'),
    ]

    title = models.CharField(max_length=200, default='Court Reservation')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date = models.DateField()
    timeslot = models.IntegerField(choices=TIMESLOTS)
    court_number = models.IntegerField(choices=COURTS)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reservation-list')
