from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:10], template_name="blog/blog.html"))
    ]