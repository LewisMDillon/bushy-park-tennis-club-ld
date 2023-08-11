from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class Reservation(models.Model):
    title = models.CharField(max_length=200, default='Court Reservation')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    date = models.DateField()
    time = models.TimeField()
    court_number = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reservation-list')
