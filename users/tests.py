import string

from django.test import TestCase
from django.contrib.auth.models import User

# from products.models import Product
# from users.models import Liked


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
