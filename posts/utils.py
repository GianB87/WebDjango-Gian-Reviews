from .models import Post
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Tag

def paginatePosts(request, posts, results, interval):
    page = request.GET.get('page')
    paginator = Paginator(posts, results)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)
    leftIndex = (int(page) - interval)

    if leftIndex < 1:
        rightIndex = (int(page) + interval + 1) - leftIndex +1
        leftIndex = 1
    else:
        rightIndex = (int(page) + interval + 1)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
    custom_range = range(leftIndex, rightIndex)
    return custom_range, posts, paginator.num_pages

def searchPosts(request):
    search_query = ''

    search_order = 'date_desc' 

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    if request.GET.get('search_order'):
        search_order = request.GET.get('search_order')

    tags = Tag.objects.filter(name__icontains=search_query)
    posts = Post.objects.distinct().filter(
        (Q(title__icontains=search_query) |
        Q(description__icontains=search_query))
        | Q(tags__in=tags)
    )
    posts = posts.order_by('-created') if search_order == 'date_desc' else posts.order_by('created') if search_order == 'date_asc' else posts.order_by('-vote_total') if search_order == 'rate_desc' else posts.order_by('vote_total')
    
    return posts, search_query, search_order