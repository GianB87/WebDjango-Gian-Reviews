from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.auth import views as auth_views
import requests

def none_fix(request):
    return render(request,'home/home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('books/', include('books.urls')),
    path('blog/', include('posts.urls')),
    path('None', none_fix)
    # path('works/', include('works.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)