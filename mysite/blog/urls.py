from django.urls import include, path
from django.views.generic import DetailView, ListView

from blog.models import Post

from . import views

urlpatterns = [ 
    path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:10], template_name="blog/blog.html")),
    path('<pk>', DetailView.as_view(model=Post, template_name="blog/post.html"))
    ]
