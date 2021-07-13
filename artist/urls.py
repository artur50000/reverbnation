from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:artist_id>/detail/', views.detail, name='detail'),
    path('addartist', views.addartist, name='addartist'),
    path('addalbum', views.addalbum, name='addalbum'),
    path('register', views.register, name='register'),
    path('signup', views.signup, name='signup'),
    path('success', views.success, name='success'),
    path('loginuser', views.loginuser, name='loginuser'),
    path("logout", views.logout_request, name="logout"),
    path("account_activation_sent", views.account_activation_sent, name='account_activation_sent'),
    path('activate/<str:uidb64>/<str:token>', views.activate, name='activate'),
   ]
