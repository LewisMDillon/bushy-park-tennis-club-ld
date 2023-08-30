import datetime

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.utils import timezone


# ------------ MODEL TESTING ------------

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


# ------------ VIEWS TESTING ------------


class WebsiteViewTestCase(TestCase):
    """
    Test case for testing webite views.
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

        post2 = Post.objects.create(
            title=title,
            subtitle=subtitle,
            content=content,
            date_posted=date_posted,
            author=author
            )

        post3 = Post.objects.create(
            title=title,
            subtitle=subtitle,
            content=content,
            date_posted=date_posted,
            author=author
            )

        post1.save()
        post2.save()
        post3.save()

    def test_home_render_context(self):
        """
        Tests that the home page is rendered properly and all of 
        the correct context is passed into the page
        """

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'website/home.html', 'website/base.html'
            )
        # Checks whether each context item is passed in
        self.assertTrue(response.context['posts'])
        self.assertTrue(response.context['latest_post'])
        self.assertTrue(response.context['second_last_post'])
        self.assertTrue(response.context['third_last_post'])

    def test_news_render_context(self):
        """
        Tests that the latest news page is rendered properly and all of 
        the correct context is passed into the page
        """

        response = self.client.get('/news')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'website/news.html', 'website/base.html'
            )
        # Checks whether each context item is passed in
        self.assertTrue(response.context['posts'])

    def test_post_detail_render_context(self):
        """
        Tests the url path by passing in the primary key of new test
        post. Checks that the post detail page is rendered properly.
        Checks that the post detail view matches the test post passed
        into the url.
        """
        # Tests the url path
        post1 = Post.objects.latest('date_posted')
        response = self.client.get(f'/post/{post1.pk}/')

        # Checks that the page renders correctly
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'website/post_detail.html', 'website/base.html'
            )

        # Cofirms that the post_detail view is
        # displaying the correct post.
        post_string_title = str(post1.title)
        post_string_author = str(post1.author)

        self.assertEqual((post_string_title), ("test_post"))
        self.assertEqual((post_string_author), ("testUser"))

    def test_post_create_render_context(self):
        """
        First, tests that the page can be accessed only by
        users with staff/superuser privileges. Next, creates
        a sample post using the page form. Lastly, checks
        that that sample post was created successfully
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

        # Try to access new post page (staff-only)
        response = self.client.get('/post/new/')

        # Check that page access is forbidden
        self.assertEqual(response.status_code, 403)

        # Log in as testUserStaff (has staff privileges)
        self.client.force_login(test_user_staff)

        # Try to access new post page (staff-only)
        response = self.client.get('/post/new/')

        # Check that page access is granted
        self.assertEqual(response.status_code, 200)

        # Check that the page renders properly
        self.assertTemplateUsed(
            response, 'website/post_form.html', 'website/base.html'
            )

        # Create a new test post using the page form
        response = self.client.post(('/post/new/'), {
            'title': 'new_test_post',
            'subtitle': 'new_test_subtitle',
            'content': 'new_test_content',
            'date_posted': datetime.datetime.now(),
            'author': test_user_staff
            })

        # Get the most recent post 
        # (should be new_test_post that we just created)
        newTestPost = Post.objects.latest('date_posted')

        post_string_title = str(newTestPost.title)
        post_string_author = str(newTestPost.author)

        # Check that the most recent post created is
        # the new_test_post, made by testUserStaff
        self.assertEqual((post_string_title), ("new_test_post"))
        self.assertEqual((post_string_author), ("testUserStaff"))

