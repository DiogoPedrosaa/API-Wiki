from django.contrib import admin
from .models import items, Item, Category, Attribute

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Attribute)