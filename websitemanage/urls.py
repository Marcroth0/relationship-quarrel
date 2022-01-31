from . import views
from django.urls import path

urlpatterns = [
    path('index.html/deactivate/',
         views.UserDeactivateView.as_view(), name='deactivate_user'),
    path('delete/', views.UserDeleteView.as_view(), name='delete_user')
]
