from .models import Book
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateBooks(request, books, results, interval):
    page = request.GET.get('page')
    paginator = Paginator(books, results)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        books = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        books = paginator.page(page)

    leftIndex = (int(page) - interval)

    if leftIndex < 1:
        leftIndex = 1
        

    rightIndex = (int(page) + interval + 1)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, books, paginator.num_pages
# def order_title(value):
#     if value == 'Low Rated First':
#         return 'rate_asc'
#     elif value == 'Oldest First':
#         return 'date_asc'
#     elif value == 'High Rated First':
#         return 'rate_desc'
#     else:
#         return 'date_desc'
def searchBooks(request):
    search_query = ''
    search_rate = ''
    search_order = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    if request.GET.get('search_rate'):
        search_rate = request.GET.get('search_rate')
    if request.GET.get('search_order'):
        search_order = request.GET.get('search_order')
    else:
        search_order = 'date_desc'
    # tags = Tag.objects.filter(name__icontains=search_query)
    if search_rate: 
        books = Book.objects.distinct().filter(
            (Q(title__icontains=search_query) |
            Q(authors__icontains=search_query) |
            Q(isbn__icontains=search_query)) & Q(rate=search_rate)
            # | Q(tags__in=tags)
        )
    else:
        books = Book.objects.distinct().filter(
            (Q(title__icontains=search_query) |
            Q(authors__icontains=search_query) |
            Q(isbn__icontains=search_query))
            # | Q(tags__in=tags)
        )
    books = books.order_by('-review_date') if search_order == 'date_desc' else books.order_by('review_date') if search_order == 'date_asc' else books.order_by('-rate') if search_order == 'rate_desc' else books.order_by('rate')
    
    return books, search_query, search_rate, search_order