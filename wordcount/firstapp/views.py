from django.shortcuts import render

# Create your views here.

# render 함수는 3개의 인자까지 받을 수 있는데 첫 번째는 고정적으로 
# request라는 객체를 받아주고, 두 번째는 템플릿의 이름, 세 번째는 사전형 자료를 받는다. 
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')