from django.contrib import admin
from django.urls import path
from . import views
from .models import Item
print(Item.objects.all())
urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    
    
]