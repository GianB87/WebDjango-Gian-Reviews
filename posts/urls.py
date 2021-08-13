from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),   
    path('post/<str:pk>/',views.post, name='post'),
    path('create-post/', views.createPost, name="create-post"),
    
] 