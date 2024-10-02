from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUserView.as_view(), name='login'),
]
