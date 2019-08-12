from django.contrib import admin
from django.urls import path
from .views import index, logout, login, profile, register
path('', index, name='index'),
path('logout/', logout, name='logout'),
path('login/', login, name='login'),
path('profile/', profile),
path('register/', register, name='register')