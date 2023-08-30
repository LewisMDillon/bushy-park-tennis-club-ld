import datetime

from django.core import mail
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Reservation
from django.utils import timezone


# ------------ MODEL TESTING ------------
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

        title = "test_reservation2"
        created_by = user2
        date_created = timezone.now()
        date = "2024-05-07"
        timeslot = 0
        court_number = 0
        reservation2 = Reservation.objects.create(
            title=title,
            created_by=created_by,
            date_created=date_created,
            date=date,
            timeslot=timeslot,
            court_number=court_number,
            )

        reservation2.save()

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

    def test_reservation_user_list_render_context(self):
        """
        First, checks that the page can only be accessed by users with
        staff privileges. Then tests that the reservation list page is
        rendered properly and all of the correct context is passed into
        the page
        """

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the user is correctly retrieved
        self.assertEqual(test_user.username, 'testUser')

        # Log in as testUser
        self.client.force_login(test_user)

        # access reservation user list page
        response = self.client.get('/reserve/reservations-user')

        # Check that the page is rendered properly
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'reservations/reservation_user_list.html',
            'website/base.html'
            )
        # Check that the context item is passed in
        self.assertTrue(response.context['reservations'])

    def test_reservation_detail_render_context(self):
        """
        Tests the url path by passing in the primary key of new test
        post. Checks that the post detail page is rendered properly.
        Checks that the post detail view matches the test post passed
        into the url.
        """
        # Tests the url path
        reservation1 = Reservation.objects.latest('date_created')
        response = self.client.get(f'/reserve/{reservation1.pk}/')

        # Checks that the page renders correctly
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'reservations/reservation_detail.html',
            'website/base.html'
            )

        # Cofirms that the reservation_detail view is
        # displaying the correct reservation.
        reservation_string_title = str(reservation1.title)
        reservation_string_created_by = str(reservation1.created_by)

        self.assertEqual((reservation_string_title), ("test_reservation"))
        self.assertEqual((reservation_string_created_by), ("testUser"))

    def test_reservation_detail_render_context(self):
        """
        Tests the url path by passing in the primary key of new test
        post. Checks that the post detail page is rendered properly.
        Checks that the post detail view matches the test post passed
        into the url.
        """
        # Tests the url path
        reservation1 = Reservation.objects.latest('date_created')
        response = self.client.get(f'/reserve/{reservation1.pk}/')

        # Checks that the page renders correctly
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            'reservations/reservation_detail.html',
            'website/base.html'
            )

        # Cofirms that the reservation_detail view is
        # displaying the correct reservation.
        reservation_string_title = str(reservation1.title)
        reservation_string_created_by = str(reservation1.created_by)

        self.assertEqual((reservation_string_title), ("test_reservation2"))
        self.assertEqual((reservation_string_created_by), ("testUserStaff"))

    def test_reservation_create_render_form(self):
        """
        Creates a sample reservation using the page form. Next,
        checks if the confirmation email is sent. Then, checks
        that that sample reservation was created successfully by
        checking that the newest reservation is not the same
        as the reservation that existed previously
        """

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the user is correctly retrieved
        self.assertEqual(test_user.username, 'testUser')

        # Log in as testUser
        self.client.force_login(test_user)

        # Get the ID of the most recently created reservation
        originalReservation = Reservation.objects.latest('date_created')
        originalReservationId = originalReservation.pk

        # Create a new test reservation using the page form
        response = self.client.post(('/reserve/new/'), {
            'title': 'new_test_reservation',
            'created_by': test_user,
            'date_created': datetime.datetime.now(),
            'date': '2024-05-06',
            'timeslot': 0,
            'court_number': 0
            })

        # Check if the confirmation email is sent
        self.assertEqual(len(mail.outbox), 1)

        # Get the most recent reservation
        # (should be new_test_reservation that we just created)
        newTestReservation = Reservation.objects.latest('date_created')
        newTestReservationId = newTestReservation.pk

        # Check that the most recent reservation created is
        # not the original reservation, meaning a new one
        # was successfully created
        self.assertNotEqual((originalReservationId), (newTestReservationId))

        # Check that the page renders properly
        response = self.client.get(f'/reserve/new/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'reservations/reservation_form.html', 'website/base.html'
            )

    def test_reservation_delete_render_form(self):
        """
        First, logs in as user who is not the creator of the reservation &
        checks that access to delete is denied. Next, logs in as the
        creator and deletes the most recent post using the delete view.
        Lastly, checks that the post was deleted successfuly.
        """

        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the two users are correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')
        self.assertEqual(test_user.username, 'testUser')

        # Get the most recent reservation
        reservationToDelete = Reservation.objects.latest('date_created')

        # Log in as testUser (not the creator of
        # the reservation)
        self.client.force_login(test_user)

        # Check that the url path works
        response = self.client.get(
            f'/reserve/{reservationToDelete.pk}/delete/'
            )

        # Check that access to the page is denied
        self.assertEqual(response.status_code, 403)

        # Log in as testUserStaff (the creator of
        # the reservation)
        self.client.force_login(test_user_staff)

        # Check that access to the page is granted
        response = self.client.get(
            f'/reserve/{reservationToDelete.pk}/delete/'
            )
        self.assertEqual(response.status_code, 200)

        # Get the to-be-deleted post's ID
        deletedReservationId = (reservationToDelete.pk)

        # Delete the post using the delete view
        response = self.client.post(
            f'/reserve/{reservationToDelete.pk}/delete/', args='1'
            )

        # Check if there are any reservations in the database,
        # if not, that means that the deletion was successful
        if Reservation.objects.exists():

            # Get the ID of the last reservation in the database
            newLastReservation = Reservation.objects.latest('date_created')
            newLastReservationId = newLastReservation.pk

            # Check if the last reservation in the database is the
            # same one that we tried to delete, if not, that
            # means the deletion was successful
            self.assertNotEqual(deletedReservationId, newLastReservationId)

    def test_date_form_render(self):
        """
        First, checks that access tothe page is denied without user login.
        Then, checks that the date form page is rendered properly when
        accessed by logged-in user
        """

        # Check that access to the page is denied without login
        # (redirected to login page, hence error 302, not 403)
        response = self.client.get('/reserve/date/')
        self.assertEqual(response.status_code, 302)

        # Get the second most recently created user (testUser)
        test_user = User.objects.filter().order_by('-pk')[1]

        # Check that the user is correctly retrieved
        self.assertEqual(test_user.username, 'testUser')

        # Log in as testUser
        self.client.force_login(test_user)

        # Check that the page is correctly rendered
        response = self.client.get('/reserve/date/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'reservations/reservation_date.html', 'website/base.html'
            )
