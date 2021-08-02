from django.shortcuts import render
from .models import Item
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login_page")
def dashboard(request):
    items = Item.objects.all()
    data = {
        'items' : items
    }
 
    return render(request, 'webpages/dashboard.html', data)





