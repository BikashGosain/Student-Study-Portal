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
# 👇 custom 404 handler
handler404 = 'account.views.custom_404'
handler400 = 'account.views.custom_400'
handler403 = 'account.views.custom_403'
handler500 = 'account.views.custom_500'
