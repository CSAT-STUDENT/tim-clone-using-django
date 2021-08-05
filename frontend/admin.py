from django.contrib import admin
from .models import Beverages, Donut, Item, Retail

# Register your models here.

admin.site.register(Item)
admin.site.register(Beverages)
admin.site.register(Donut)
admin.site.register(Retail)
