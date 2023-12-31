from django.test import TestCase
from django.contrib.auth.models import User

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


# ------------ MODEL TESTING ------------
class TestUserProfile(TestCase):
    """Tests the models for the Users app."""
    def setUp(self):
        """Creates a newly signed up user and declares some profile details."""

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

    def test_str(self):
        """Tests the string method on the UserProfile."""
        # Retrieves the most recently created user and gets their string
        user1 = User.objects.latest('date_joined')
        user_string_username = str(user1.username)
        user_string_email = str(user1.email)
        user_string_password = str(user1.password)
        user_string_first_name = str(user1.first_name)
        user_string_last_name = str(user1.last_name)

        # Cofirms the userprofile string is correct.
        self.assertEqual((user_string_username), (user1.username))
        self.assertEqual((user_string_email), (user1.email))
        self.assertEqual((user_string_password), (user1.password))
        self.assertEqual((user_string_first_name), (user1.first_name))
        self.assertEqual((user_string_last_name), (user1.last_name))


# ------------ VIEWS TESTING ------------

class TestUserViews(TestCase):
    """Tests views for the Users app."""

    def setUp(self):
        """
        Creates two sample users, one of whom has staff & superuser
        privileges (testUserStaff) and another who does not (testUser).
        Then creates three sample posts for testing.
        """

        username = "testUserStaff"
        email = "testuser2@test.com"
        password = "default123"
        first_name = "Test"
        last_name = "User"

        user1 = User.objects.create(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
            )

        user1.is_staff = True
        user1.is_superuser = True

        user1.profile.save()
        user1.save()

    def test_user_register(self):
        """
        First, tests that the register page is rendered correctly.
        Then, creates a new test user using the register view form.
        Lastly, checks that the user was created successfully
        """
        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Check that the user is correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')

        # Check that the register page is rendered correctly
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

        # Register a new test user using the page form
        response = self.client.post(('/register/'), {
            'username': 'newTestUser',
            'first_name': 'test',
            'last_name': 'user',
            'email': 'test@test.com',
            'password1': 'default123',
            'password2': 'default123'
            })

        # Check if the newest user in the database is our
        # newTestUser which was just created, and not testUserStaff,
        # which it was previously
        newest_user = User.objects.latest('date_joined')
        self.assertEqual(newest_user.username, 'newTestUser')

    def test_user_profile_login_render_form(self):
        """
        First, tests that the profile page can be accessed
        only by logged in users. Next, checks that the profile
        page renders correctly. Then, updates the logged-in user's
        profile details using the view form. Lastly, checks that
        the user's profile details were updated successfully
        """
        # Get the most recently created user (testUserStaff)
        test_user_staff = User.objects.latest('date_joined')

        # Check that the user is correctly retrieved
        self.assertEqual(test_user_staff.username, 'testUserStaff')

        # Check that page cannot be accessed without user login
        # (redirects to login page, hence error 302, not 403)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)

        # Log in as testUserStaff
        self.client.force_login(test_user_staff)

        # Check that page access is granted
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

        # Check that the page renders properly
        self.assertTemplateUsed(
            response, 'users/profile.html', 'website/base.html'
            )

        # Updates testUserStaff's profile with new details
        # using the profile view form
        response = self.client.post(('/profile/'), {
            'first_name': 'TestUpdated',
            'last_name': 'UserUpdated',
            'username': 'testUserStaffUpdated',
            'email': 'testuser2updated@test.com',
            'password1': 'default123',
            'password2': 'default123'
            })

        # Check if testUserStaff's details have been successfully updated
        test_user_staff_updated = User.objects.latest('date_joined')
        self.assertEqual(
            test_user_staff_updated.first_name, 'TestUpdated'
            )
        self.assertEqual(
            test_user_staff_updated.last_name, 'UserUpdated'
            )
        self.assertEqual(
            test_user_staff_updated.username, 'testUserStaffUpdated'
            )
        self.assertEqual(
            test_user_staff_updated.email, 'testuser2updated@test.com'
            )
