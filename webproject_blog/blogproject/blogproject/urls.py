from django.contrib import admin
from django.urls import path
import blogapp.views
import portfolio.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name = "home"),
    path('blog/<int:blog_id>', blogapp.views.detail, name = "detail"),
    path('blog/new/', blogapp.views.new, name = "new"),
    path('blog/create', blogapp.views.create, name = "create"), #html을 띄운다는 것이 아니라 create 함수를 실행시킨다는 뜻
    path('portfolio/', portfolio.views.portfolio, name = "portfolio"),
    ]
