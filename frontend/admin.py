from django.contrib import admin
from .models import Donut, Item, Retail, Beverages_updated, Lunch, Special

# Register your models here.
admin.site.register(Item)
admin.site.register(Beverages_updated)
admin.site.register(Donut)
admin.site.register(Retail)
admin.site.register(Lunch)
admin.site.register(Special)