import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Reservation
from django.utils import timezone


class TestReservation(TestCase):
    """Tests the model for the reservations app."""
    def setUp(self):
        """
        First creates a test user who will make the reservation, then makes
        a sample reservation.
        """

        username = "testUser"
        email = "testuser@test.com"
        password = "default123"
        first_name = "Test"
        last_name = "User"
        user1 = User.objects.create(username=username,
                                    email=email,
                                    password=password,
                                    first_name=first_name,
                                    last_name=last_name)

        user1.profile.save()

        title = "test_reservation"
        created_by = user1
        date_created = timezone.now()
        date = "2023-11-11"
        timeslot = 0
        court_number = 0
        reservation1 = Reservation.objects.create(
            title=title,
            created_by=created_by,
            date_created=date_created,
            date=date,
            timeslot=timeslot,
            court_number=court_number,
            )

        reservation1.save()

    def test_str(self):
        """Tests the string method on the reservation."""
        # Retrieves the most recently created reservation and gets its string
        reservation1 = Reservation.objects.latest('date_created')
        reservation_string_title = str(reservation1.title)

        # Cofirms the reservation string is correct.
        self.assertEqual((reservation_string_title), (reservation1.title))
