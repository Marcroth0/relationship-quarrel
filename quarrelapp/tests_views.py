from django.test import TestCase, Client
from django.urls import reverse
from quarrelapp.models import CommentPost, Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestQuarrelViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test@test.com',
            email='test@test.com', password='12345678')
        self.client.login(
            username='test@test.com',
            email='test@test.com', password='12345678')

    def test_post_creation(self):
        comment_one = CommentPost(content='Whatever')
        comment_two = CommentPost(content='Whats up')
        # import pdb
        # pdb.set_trace()
        post = Post(content_one=comment_one,
                    content_two=comment_two, description='A description')
        self.assertEqual(post.description, 'A description')
        self.assertEqual(post.content_one.content, 'Whatever')

    # def test_like_function(self, request):
    #     post = get_object_or_404(Post)
    #     content_one = post.content_one.likes.add(request.user)

    #     self.assertTrue(content_one.likes.filter(
    #         id=request.user.id).exists())
