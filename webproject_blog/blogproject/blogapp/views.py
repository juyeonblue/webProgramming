from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'blogapp/home.html', {'blogs' : blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blogapp/detail.html', {'details': details})

def new(request):
    return render(request, 'blogapp/new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #blog객체에 해당하는 내용을 저장해라
    return redirect('/blog/' + str(blog.id)) #위의 내용을 이 url로 넘기세요 
    #url은 항상 정수형인데 id는 인트형이므로 str을 사용하여 형 변환한다
    