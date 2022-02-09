from django.test import SimpleTestCase
from django.urls import reverse, resolve
from quarrelapp.views import PostList, PostDetail, UserPost, PostLike, PostEdit


class TestUrls(SimpleTestCase):
    def test_home_url_is_resolved(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_create_url_is_resolved(self):
        url = reverse('user_post')
        self.assertEquals(resolve(url).func.view_class, UserPost)

    def test_postview_url_is_resolved(self):
        url = reverse('post_detail', args=['post-id'])
        self.assertEquals(resolve(url).func.view_class, PostDetail)

    # def test_postlike_url_is_resolved(self):
    #     url = reverse('post_like', args=[id])
    #     self.assertEquals(resolve(url).func.view_class, PostLike)

    # def test_post_edit_url_is_resolved(self):
    #     url = reverse('edit_post', args=['slug'])
    #     self.assertEquals(resolve(url).func, PostEdit)

    # def test_delete_comment_url_is_resolved(self):
    #     url = reverse('delete_comment', args=['post-id'])
    #     self.assertEquals(resolve(url).func.view_class, PostDetail)
