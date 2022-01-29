from . import views
from django.urls import path
from .views import UserPost


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.UserPost.as_view(), name='user_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]
