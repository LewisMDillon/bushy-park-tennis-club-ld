import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone


class TestPost(TestCase):
    """Tests the post model in the website app."""
    def setUp(self):
        """
        First creates a test user who will make the post, then makes
        a sample post.
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

        title = "test_post"
        subtitle = "test_subtitle"
        content = "test_content"
        date_posted = timezone.now()
        author = user1
        post1 = Post.objects.create(
            title=title,
            subtitle=subtitle,
            content=content,
            date_posted=date_posted,
            author=author
            )

        post1.save()

    def test_str(self):
        """Tests the string method on the post."""
        # Retrieves the most recently created post and gets its string
        post1 = Post.objects.latest('date_posted')
        post_string_title = str(post1.title)

        # Cofirms the reservation string is correct.
        self.assertEqual((post_string_title), (post1.title))
        