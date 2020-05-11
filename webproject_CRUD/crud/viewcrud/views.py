from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Blog
from .forms import NewBlog

def welcome(request):
    return render(request, 'viewcrud/index.html')

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'blogs': blogs})

def update(request):
    return

def delete(request):
    return

def create(request): 
    # 새로운 데이터 블로그 글 저장하는 역할 == POST
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return redirect('home')

    else: #글쓰기 페이지를 띄어주는 역할 == GET
        form = NewBlog()
        return render(request, 'viewcrud/new.html', {'form': form})