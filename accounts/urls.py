from django.urls import path
from django.shortcuts import render
from .views import dashboard, register, user_login, user_logout
from . import views


urlpatterns = [

    path(
        'register/',
        register,
        name='register'
    ),

    path(
        'login/',
        user_login,
        name='login'
    ),

    path(
    'dashboard/',
    dashboard,
    name='dashboard'
    ),
    
    path(
    'logout/',
    user_logout,
    name='logout'   
    ),

    path(
    'forgot-password/',
    views.forgot_password,
    name='forgot_password'
),

    path(
    'reset-password/',
    views.reset_password,
    name='reset_password'
),


]

