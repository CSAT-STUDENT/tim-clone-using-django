from django.contrib import admin
from django.urls import path
from . import views
from .models import Item

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cold', views.cold, name='COLD'),
    path('hot', views.hot, name='HOT'),
    path('lunch', views.lunch, name='LUNCH'),
    path('special', views.special, name='SPECIAL'),
    path('donut', views.donut, name="DONUT")
    
    
]