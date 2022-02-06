from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.UserPost.as_view(), name='user_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    #     path('<slug:slug>/list', views.PostDetailList.as_view(),
    #          name="post_detail_list"),
    path('like/<slug:slug>/<int:id>', views.PostLike.as_view(), name='post_like'),
    path('edit_post/<slug:slug>/', views.PostEdit.edit_post, name='edit_post'),
    path('delete/<int:id>', views.PostDetail.delete_own_comment,
         name='delete_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
