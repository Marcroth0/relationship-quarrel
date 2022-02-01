from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.UserPost.as_view(), name='user_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/<int:id>',
         views.PostLike.as_view(), name='post_like')
]
