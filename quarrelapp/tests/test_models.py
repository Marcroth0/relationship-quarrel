from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from quarrelapp.models import Post, CommentPost, Comment


class PostModelTestCase(TestCase):
    def setUp(self):
        # Disconnect signal from haystack, no need to generate
        # index for test generated articles
        # apps.get_app_config('haystack').signal_processor.teardown()
        self.user = User.objects.create_user(
            username="admin", email="admin@hellogithub.com", password="123!!"
        )
        self.login = self.client.login(username="admin", password="123!!")
        self.contentOne = CommentPost.objects.create(
            content="content one test",
        )
        self.contentTwo = CommentPost.objects.create(
            content="content two test")

        self.post = Post.objects.create(
            title="CLEANING",
            content_one=self.contentOne,
            content_two=self.contentTwo,
            description="Test description",
            user=self.user,
        )

    def test_post_create_01(self):
        testpost = get_object_or_404(Post, title="CLEANING")
        self.assertEqual(self.post.content_one, testpost.content_one)

        self.assertEqual(self.post.content_two, testpost.content_two)

        self.assertEqual(self.post.description, "Test description")

        self.assertNotEqual(self.post.content_two, testpost.content_one)

        self.assertNotEqual(self.post.description, "Descriptionz")

        self.assertEqual(self.post.title, "CLEANING")

        self.assertEqual(self.post.date_published, testpost.date_published)

    def test_add_comment(self):
        post = get_object_or_404(Post, title="CLEANING")
        self.comment = Comment.objects.create(
            post=post, body="This is my comment"
        )
        self.assertEqual(self.comment.body, "This is my comment")

        self.assertNotEqual(self.comment.body, "Not my comment")

        self.assertIsNotNone(self.comment.post_id)

        self.assertEqual(self.comment.post_id, post.id)

        self.assertIsNotNone(self.comment.date_published)

    def test_add_like(self):
        post = get_object_or_404(Post, title="CLEANING")
        post.content_one.likes.add(self.user)

        self.assertEqual(post.content_one.number_of_likes(), 1)
