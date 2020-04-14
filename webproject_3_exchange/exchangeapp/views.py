from django.shortcuts import render

def home(request):
    return render(request,'exchangeapp/home.html')

def usd(request):
    korea = request.POST['korea']
    korea = int(korea)
    usd = korea/1215.50
    return render(request,'exchangeapp/usd.html',{'korea':korea,'usd':usd})

def jpy(request):
    korea = request.POST['korea']
    korea = int(korea)
    jpy = korea/1131.38*100
    return render(request,'exchangeapp/jpy.html',{'korea':korea,'jpy':jpy})

def can(request):
    korea = request.POST['korea']
    korea = int(korea)
    can = korea/873.33
    return render(request,'exchangeapp/can.html',{'korea':korea,'can':can})