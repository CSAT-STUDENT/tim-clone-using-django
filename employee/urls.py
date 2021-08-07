from django.contrib import admin
from django.urls import path
from . import views
from .models import Employee

urlpatterns = [
    path('', views.listemp, name='listemp'),
    path('<str:name>', views.listempspecific, name='listempspecific'),
    path('add/', views.addemp, name='addemp')
   
    
    
]