
from os import name
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.dash,name='Dashboard'),
    path('react',views.react,name='React'),
    path('drop',views.reactDrop,name='Drop')
]