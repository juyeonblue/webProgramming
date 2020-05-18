from django.shortcuts import render

def home(request):
    return render(request, 'accounts/login.html', name = 'login')

def signup(request):
    return render(request, 'accounts/signup.html', name= 'signtup')