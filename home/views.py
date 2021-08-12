from django.shortcuts import render
from books.models import Book
from django.db.models import Q
from .utils import get_yt_video_id

from posts.models import Post
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
