from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', myapp.views.index),
    path('lions/', myapp.views.lion_list, name = 'lions'),
    # url에 'lions/'이 입력되면 myapp/views.py에 있는 lion_list 함수를 호출해준다
]

