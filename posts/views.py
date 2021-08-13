from django import urls
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
# import book model
from .utils import searchPosts, paginatePosts
from .forms import PostForm
from .models import Tag, Post 
# Create your views here.

def blog(request):
    posts, search_query,  search_order = searchPosts(request)
    custom_range, posts, num_pages = paginatePosts(request, posts, results=5, interval = 3)
    postPop = Post.objects.all().order_by('-vote_total')[:3]
    context = {'posts': posts,
               'search_query': search_query,
               'pops':postPop,
               'custom_range': custom_range,
               'search_order': search_order, 'num_pages': num_pages}
    return render(request,'posts/blog.html', context)

def post(request,pk):
    postObj = Post.objects.get(id=pk)
    context = {'post': postObj, 
                'max':range(10)}
    return render(request, 'posts/single-post.html',context)
    
@login_required(login_url='home')
def createPost(request):
    profile = request.user.profile
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = profile
            form.save()
            return redirect('blog')
    context = {'form': form}
    return render(request, "posts/post_form.html", context)
