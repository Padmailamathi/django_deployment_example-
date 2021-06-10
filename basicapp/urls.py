from django.conf.urls import url
from django.urls import include, path
from basicapp import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('base', views.base,name='base'),
    path('register', views.register,name='register'),
]
