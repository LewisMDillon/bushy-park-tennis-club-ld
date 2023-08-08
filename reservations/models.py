from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Reservation(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    reservation_time = models.DateTimeField()
    court_number = models.IntegerField()

    def __str__(self):
        return self.title
