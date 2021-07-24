from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.add, name ='add'),
    path('choose/<vote_id>/', views.choose, name='choose'),
    path('result/<vote_id>/', views.result, name='result'),
]