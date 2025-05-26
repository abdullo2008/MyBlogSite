from django.contrib.auth.views import LoginView
from django.urls import path
from .views import LoginPage, LogoutPage, register

urlpatterns = [
    path('login/', LoginPage, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutPage, name='logout'),

]
