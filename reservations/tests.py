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


# ------------ VIEWS TESTING ------------

class ReservationViewTestCase(TestCase):
    """
    Test case for testing reservation views.
    """

    def setUp(self):
        """
        Creates two sample users, one of whom has staff & superuser
        privileges (testUserStaff) and another who does not (testUser).
        Then creates three sample posts for testing.
        """

        username1 = "testUser"
        email1 = "testuser@test.com"
        password = "default123"
        first_name = "Test"
        last_name = "User"

        username2 = "testUserStaff"
        email2 = "testuser2@test.com"
        password = "default123"
        first_name = "Test"
        last_name = "User"

        user1 = User.objects.create(
            username=username1,
            email=email1,
            password=password,
            first_name=first_name,
            last_name=last_name
            )

        user2 = User.objects.create(
            username=username2,
            email=email2,
            password=password,
            first_name=first_name,
            last_name=last_name
            )

        user2.is_staff = True
        user2.is_superuser = True

        user1.profile.save()
        user2.profile.save()
        user2.save()

        title = "test_reservation"
        created_by = user1
        date_created = timezone.now()
        date = "2024-05-05"
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

    def test_reservation_list_staff_render_context(self):
        """
        First, checks that the reservation list page can only be
        accessed by users with staff privileges. Then tests that the
        page is rendered properly and all of the correct context is
        passed into the page
        """

        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the two users are correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')
        self.assertEqual(test_user.username, 'testUser')

        # Log in as testUser (no staff privileges)
        self.client.force_login(test_user)

        # Try to access reservation list page (staff-only)
        response = self.client.get('/reserve/')

        # Check that page access is forbidden
        self.assertEqual(response.status_code, 403)

        # Log in as testUserStaff (has staff privileges)
        self.client.force_login(test_user_staff)

        # Try to access reservation list page (staff-only)
        response = self.client.get('/reserve/')

        # Check that page access is granted
        self.assertEqual(response.status_code, 200)

        # Check that the page is rendered properly
        response = self.client.get('/reserve/')
        self.assertTemplateUsed(
            response, 'reservations/reservation_list.html', 'website/base.html'
            )
        # Check that the context item is passed in
        self.assertTrue(response.context['reservations'])

