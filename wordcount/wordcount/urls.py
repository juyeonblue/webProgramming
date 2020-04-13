from django.contrib import admin
from django.urls import path
import firstapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', firstapp.views.home, name="home"),
    path('about/', firstapp.views.about, name="about"),
]
