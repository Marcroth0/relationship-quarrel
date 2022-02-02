from django.test import SimpleTestCase
from django.urls import reverse, resolve
from websitemanage.views import UserDeactivateView, UserDeleteView, profile, PostDeleteView


# class TestWebsiteManageUrls(SimpleTestCase):
#     # def test_deactivate_user_url_is_resolved(self):
#     #     url = reverse('deactivate_user')
#     #     self.assertEquals(resolve(url).func.view_class, UserDeactivateView)

#     # def test_delete_user_url_is_resolved(self):
#     #     url = reverse('delete_user')
#     #     self.assertEquals(resolve(url).func.view_class, UserDeleteView)

#     # def test_profile_url_is_resolved(self):
#     #     url = reverse('profile')
#     #     self.assertEquals(resolve(url).func, profile)

#     # def test_profile_url_is_resolved(self):
#     #     url = reverse('delete')
#     #     self.assertEquals(resolve(url).func.view_class,
#     #                       PostDeleteView.delete_post)
