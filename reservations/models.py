from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Reservation(models.Model):
    title = models.CharField(max_length=200, default='Court Reservation')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    court_number = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reservation')
