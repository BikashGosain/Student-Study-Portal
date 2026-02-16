from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [


    # User registration
    path('SignupPage/', views.SignupPage, name='SignupPage'),

    # User login using Django's built-in view
    path('LoginPage/', views.LoginPage, name='LoginPage'),

    # User logout
    path('LogoutPage/', views.LogoutPage, name='LogoutPage'),
]
