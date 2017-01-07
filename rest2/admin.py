from django.contrib import admin

# Register your models here.

from rest2.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)