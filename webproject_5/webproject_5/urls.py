from django.contrib import admin
from django.urls import path, include
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name = 'home'),
    path('lions/', myapp.views.lion_list, name = 'lions'),
    path('lions/<int:pk>', myapp.views.lion_posts, name = 'lion_posts'),
    path('post/', include('post.urls')) 
    # url에 'lions/'이 입력되면 myapp/views.py에 있는 lion_list 함수를 호출해준다
]

