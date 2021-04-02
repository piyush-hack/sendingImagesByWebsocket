# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [

    path('base/', views.base, name='base'),
    path('test/', views.test, name='test'),

    path('', views.index, name='index'),

]