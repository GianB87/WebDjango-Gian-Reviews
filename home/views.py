from django import urls
from django.shortcuts import redirect, render
from books.models import Book
from django.db.models import Q
from .utils import get_yt_video_id
from django.http import HttpResponse
from posts.models import Post
from django import forms
from django.urls import resolve
from django.shortcuts import redirect,render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from users.models import User

def logoutUser(request):
    current_url = resolve(request.path_info).url_name
    logout(request)
    return redirect(request.META.get('HTTP_REFERER'))
def loginCheck(request): 
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        return redirect('home')
    if request.method =='POST':
        
        print(request.META['HTTP_REFERER'])
        print('hi')
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # this is how we establish an user is login
            messages.success(request,"User Login Successfull")
            return HttpResponse('Reload') 
        else:
            messages.error(request,"Invalid Credential")
            return HttpResponse('Invalid Credential')
values = {0: 'NOT RATED',
        1: 'DO NOT READ',
        2: 'VERY BAD',
        3: 'BAD',
        4: 'MEDIOCRE',
        5: 'SO SO',
        6: 'FINE',
        7: 'GOOD',
        8: 'VERY GOOD',
        9: 'GREAT',
        10:'MASTERWORK'}


def home(request):

    if request.method =='POST':
        current_url = resolve(request.path_info).url_name
        print(request.META['HTTP_REFERER'])
        print('hi')
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # this is how we establish an user is login
            messages.success(request,"User Login Successfull")
            return redirect(current_url)
            return HttpResponse(request.META['HTTP_REFERER']+'#') & render(request,'home/home.html')
        else:
            messages.error(request,"Invalid Credential")
            raise forms.ValidationError

    # if request.method =='POST':
    #     print('hi')
    #     return loginCheck(request)
    bookObjs =Book.objects.all()
    new_books = bookObjs.order_by('-review_date')[:3]
    top_rated = bookObjs.order_by('-rate')[:12]
    comming = bookObjs.distinct().filter(Q(rate=0))[:12]
    newest = bookObjs.order_by('-review_date')[:12]
    newest_posts = Post.objects.all().order_by('-created')[:3]

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
