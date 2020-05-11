from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'blogapp/home.html', {'blogs' : blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogapp/detail.html', {'details': details})

