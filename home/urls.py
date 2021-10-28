from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('login',views.loginuser, name='home'),
    path('',views.index, name='home'),
    path('index.html',views.index,name='index'),
    path('logoutuser',views.logout, name='logout')
]   