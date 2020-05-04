from django.shortcuts import render
from myapp.models import Lion

def index(request):
    return render(request, 'index.html') 

def lion_list(request):
    lion_list = Lion.objects.all()

    return render(request, 'lions.html', {'lion_list' : lion_list})