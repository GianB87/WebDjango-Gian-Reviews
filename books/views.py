from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests

from django.views.generic.edit import CreateView
# import book model
from .models import Book
from .forms import BookForm
from .utils import searchBooks, paginateBooks


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

def books(request): 
    books, search_query, search_rate, search_order = searchBooks(request)
    custom_range, books, num_pages = paginateBooks(request, books, results=12, interval = 3)

    context = {'books': books,
               'search_query': search_query,'ratings': values, 
               'search_rate':search_rate, 'custom_range': custom_range,
               'search_order': search_order, 'num_pages': num_pages}
    return render(request, 'books/books.html',context)
 
def book(request, pk):
    bookObj = Book.objects.get(id=pk)

    context = {'book': bookObj, 'max':range(10)}
    return render(request, 'books/book-review.html', context) 


def createBook(request):
    form = BookForm()
 
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)

            book_data = requests.get('https://www.googleapis.com/books/v1/volumes?q=isbn:' + str(book.isbn)).json()
            book.title = book_data['items'][0]['volumeInfo']['title']
            authors = book_data['items'][0]['volumeInfo']['authors']
            book.authors = ' - '.join([str(elem) for elem in authors])
            book.image_link = book_data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
            book.save()
            return redirect('books')
    context = {'form': form}
    return render(request, "books/book-form.html", context)