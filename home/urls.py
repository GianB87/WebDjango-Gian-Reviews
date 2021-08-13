from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),   
    path('about/', views.about, name='about') ,
    path('login/', views.loginCheck, name='login'),
    path('logout/', views.logoutUser, name='logout')
] 