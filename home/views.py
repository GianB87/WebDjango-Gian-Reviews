from django import urls
from django.shortcuts import redirect, render
from books.models import Book
from django.db.models import Q
from .utils import *
from django.http import HttpResponse
from posts.models import Post
from django import forms
from django.urls import resolve
from django.shortcuts import redirect,render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from users.models import User

def logoutUser(request):
    messages.info(request, 'Goodbye ' + request.user.username.capitalize() + ', nice travel.')
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))
def loginUser(request): 
    if request.user.is_authenticated:
        return redirect('home')
    return loginPostHttp(request)
def registerUser(request):
    return registerPostHttp(request)

def home(request):

    bookObjs =Book.objects.all()
    new_books = bookObjs.order_by('-review_date')[:3]
    top_rated = bookObjs.order_by('-rate')[:12]
    comming = bookObjs.distinct().filter(Q(rate=0))[:12]
    newest = bookObjs.order_by('-review_date')[:12]
    newest_posts = Post.objects.all().order_by('-created')[:3]
    
    #^ add case when image or link not found (https://stackoverflow.com/questions/7995080/html-if-image-is-not-found)
    #^ add ckeditor ability to insert code (https://www.youtube.com/watch?v=L6y6cn1XUfw)
    #^ add filter view for three kind of videos (https://stackoverflow.com/questions/56109878/best-way-to-write-views-for-multiple-queries-in-django)
    book_videos = bookObjs.exclude(youtube_link__isnull=True).order_by('-review_date')[:6]
    youtube_ids = [get_yt_video_id(i) for i in book_videos.values_list('youtube_link', flat=True)]
    imgs = ["http://img.youtube.com/vi/%s/0.jpg" % id for id in youtube_ids]
    links = ["https://www.youtube.com/embed/" + id for id in youtube_ids]
    context = {'book_items':new_books, 
                'ratings':values, 'top_rated':top_rated, 
                'comming':comming,'newest':newest,
                'imgs': imgs,
                'links': links,
                'newest_posts':newest_posts,
                }
    return render(request, 'home/home.html',context)

def about(request):
    return render(request, 'home/about.html')
