from django.contrib import admin
from .models import Beverages, Item

# Register your models here.

admin.site.register(Item)
admin.site.register(Beverages)
