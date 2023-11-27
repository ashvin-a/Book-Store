from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('title')
    return render(request,"page/index.html",{
        "posts" : posts
    })

def blog_detail(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request,"page/blog.html",{
        "title":post.title,
        "author":post.author,
        "excerpt":post.excerpt,
        "image_name":post.image_name,
        "date":post.date,
        "content":post.content
    })
    