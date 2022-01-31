from . import views
from django.urls import path

urlpatterns = [
    path('deactivate/',
         views.UserDeactivateView.as_view(), name='deactivate_user'),
    path('delete/', views.UserDeleteView.as_view(), name='delete_user'),
    path('profile/', views.profile.as_view(), name='profile'),
]
