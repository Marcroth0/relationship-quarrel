from django.forms import SlugField
from django.test import TestCase, Client
from django.urls import reverse
from quarrelapp.models import CommentPost, Post, Comment
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestQuarrelViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.postdetail_url = reverse('post_detail', args=[333])
        self.user = User.objects.create_user(
            username='test@test.com',
            email='test@test.com', password='12345678')
        self.client.login(
            username='test@test.com',
            email='test@test.com', password='12345678')

        self.post = Post.objects.create(
            title='CLEANING',
            description='A quarrel',
            content_one=CommentPost(content='First content'),
            content_two=CommentPost(content='Second content'),
            post_id='333'
        )

        self.postdetail_url = reverse('post_detail', args=[333])

    def test_post_creation(self):
        comment_one = CommentPost(content='Whatever')
        comment_two = CommentPost(content='Whats up')
        # import pdb
        # pdb.set_trace()
        post = Post(content_one=comment_one,
                    content_two=comment_two, description='A description')
        self.assertEqual(post.description, 'A description')
        self.assertEqual(post.content_one.content, 'Whatever')

    def test_postdetail(self):
        response = self.client.get(self.postdetail_url)
        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'post_detail.html')
    # def test_like_function(self, request):
    #     post = get_object_or_404(Post)
    #     content_one = post.content_one.likes.add(request.user)

    #     self.assertTrue(content_one.likes.filter(
    #         id=request.user.id).exists())

    # def test_like_function(self):
    #     """Test Coach list view"""
    #     response = self.client.get('/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'index.html')
