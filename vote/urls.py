from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name ='add'),
    path('choose/', views.choose, name='choose'),
    path('result/', views.result, name='result'),
]