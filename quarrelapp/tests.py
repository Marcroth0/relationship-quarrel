from pdb import set_trace
from django.test import TestCase
from .models import Post, CommentPost


class PostTestCase(TestCase):
    def test_post_creation(self):
        """Animals that can speak are correctly identified"""
        comment_one = CommentPost(content='Whatever')
        comment_two = CommentPost(content='Whats up')
        # import pdb
        # pdb.set_trace()
        post = Post(content_one=comment_one,
                    content_two=comment_two, description='A description')
        self.assertEqual(post.description, 'A description')
        self.assertEqual(post.content_one.content, 'Whatever')
