from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:artist_id>/detail/', views.detail, name='detail'),
    path('addartist', views.addartist, name='addartist'),
    path('addalbum', views.addalbum, name='addalbum'),
    path('register', views.register, name='register'),
    path('success', views.success, name='success'),
    path('loginuser', views.loginuser, name='loginuser'),
    path("logout", views.logout_request, name="logout"),
   ]
