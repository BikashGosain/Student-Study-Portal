from django.urls import path
from django.contrib.auth import views as auth_views
from dashboard import views as dashboard_views
from . import views

urlpatterns = [
    path('', dashboard_views.home, name='home'),

    # User registration
    path('SignupPage/', views.SignupPage, name='SignupPage'),

    # User login using Django's built-in view
    path('LoginPage/', views.LoginPage, name='LoginPage'),

    # User logout
    path('LogoutPage/', views.LogoutPage, name='LogoutPage'),
]
