from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name="books"),
    path('book/<str:pk>/', views.book, name="book"), 
    path('create-book/', views.createBook, name="create-book"),   
] 