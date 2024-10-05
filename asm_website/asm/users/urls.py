from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('regisetr_done/', views.register_done, name='register_done')
]
