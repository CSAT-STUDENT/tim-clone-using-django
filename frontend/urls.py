from django.contrib import admin
from django.urls import path
from . import views
from .models import Item

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cold', views.cold, name='cold'),
    path('hot', views.hot, name='hot'),
    path('lunch', views.lunch, name='lunch'),
    path('special', views.special, name='special'),
    path('donut', views.donut, name="donut")
    
    
]