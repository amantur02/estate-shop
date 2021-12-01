from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register, profile, profile_detail, about

urlpatterns = [
    path('about', about, name='about'),
    path('profile-detail/<int:pk>/', profile_detail, name='profile_detail'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
