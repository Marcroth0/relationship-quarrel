from django.apps import apps
from django.test import TestCase
from django.contrib.auth.models import User


class PostModelTestCase(TestCase):
    def setUp(self):
        # Disconnect signal from haystack, no need to generate index for test generated articles
        apps.get_app_config('haystack').signal_processor.teardown()
        user = User.objects.create_superuser(
            username='admin',
            email='admin@hellogithub.com',
            password='admin')
        cate = Category.objects.create(name='Test')
        self.post = Post.objects.create(
            title='Test title',
            body='Test content',
            category=cate,
            author=user,
        )

    def test_str_representation(self):
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_auto_populate_modified_time(self):
        self.assertIsNotNone(self.post.modified_time)

        old_post_modified_time = self.post.modified_time
        self.post.body = 'New test content'
        self.post.save()
        self.post.refresh_from_db()
        self.assertTrue(self.post.modified_time > old_post_modified_time)

    def test_auto_populate_excerpt(self):
        self.assertIsNotNone(self.post.excerpt)
        self.assertTrue(0 < len(self.post.excerpt) <= 54)

    def test_get_absolute_url(self):
        expected_url = reverse('blog:detail', kwargs={'pk': self.post.pk})
        self.assertEqual(self.post.get_absolute_url(), expected_url)

    def test_increase_views(self):
        self.post.increase_views()
        self.post.refresh_from_db()
        self.assertEqual(self.post.views, 1)

        self.post.increase_views()
        self.post.refresh_from_db()
        self.assertEqual(self.post.views, 2)
