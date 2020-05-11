from django.shortcuts import render
from django.utils import timezone

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClassBlog

#generic view 마음대로 html템플릿 이름을 생성할 수 없다. 이름이 고정되어 있음.

class BlogView(ListView): #(소문자모델)_list.html
    model = ClassBlog

class BlogCreate(CreateView): #(소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDetail(DeleteView): #(소문자모델)_detail.html
    model = ClassBlog

class BlogUpdate(UpdateView): #(소문자모델)_form.html
    model = ClassBlog
    fields = ['title', 'body']
    success_url = reverse_lazy('list')

class BlogDelete(DeleteView): #(소문자모델)_confirm_delete.html
    model = ClassBlog
    success_url = reverse_lazy('list')

