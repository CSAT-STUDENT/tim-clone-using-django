from django.shortcuts import render
from .models import Item,Donut,Beverages_updated,Lunch,Special
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login_page")
def dashboard(request):
    items = Item.objects.all()
    data = {
        'items' : items
    }
 
    return render(request, 'webpages/dashboard.html', data)


@login_required(login_url="login_page")
def cold(request):
    cold_items = Beverages_updated.objects.filter(type='COLD')
    data = {
        'cold_items' : cold_items
    }
    return render(request, 'webpages/cold.html', data)


@login_required(login_url="login_page")
def hot(request):
    hot_items = Beverages_updated.objects.filter(type='HOT')
    data = {
        'hot_items' : hot_items
    }
    return render(request, 'webpages/hot.html', data)

@login_required(login_url="login_page")
def lunch(request):
    lunch_items  = Lunch.objects.all()
    data = {
        'lunch_items' : lunch_items
    }
    return render(request, 'webpages/lunch.html', data)

@login_required(login_url="login_page")
def special(request):
    special_items  = Special.objects.all()
    data = {
        'special_items' : special_items
    }
    return render(request, 'webpages/special.html', data)


@login_required(login_url="login_page")
def donut(request):
    donut_items  = Donut.objects.all()
    data = {
        'donut_items' : donut_items
    }
    return render(request, 'webpages/donut.html', data)
