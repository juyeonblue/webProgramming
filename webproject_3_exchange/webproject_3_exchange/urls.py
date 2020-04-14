from django.contrib import admin
from django.urls import path
import exchangeapp.views
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', exchangeapp.views.home, name="home"),
    path('usd/', exchangeapp.views.usd, name="usd"),
    path('jpy/', exchangeapp.views.jpy, name="jpy"),
    path('can/', exchangeapp.views.can, name="can"),
   
]

