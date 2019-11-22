from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.coreHome, name='coreHome'),
    path('listaCliente/', views.listaCliente, name='listaCliente'),

]
