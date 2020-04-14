from django.shortcuts import render
from myapp.models import Lion # 등록한 model인 Lion을 import 해주고

def lion_list(request): 
    lion_list = Lion.objects.all()  # Lion모델에있는 objects(이름)를 all(모두) 가져와라

    return render(request, 'myapp/lions.html', {'lion_list' : lion_list})
    # lions.html을 render 해줄껀데 선언하고 할당해준 lion_list 변수를 html에 넘겨준다.


