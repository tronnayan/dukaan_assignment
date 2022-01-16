from django.contrib import admin
from .models import Store, Categories, Products, Order, Cart
# Register your models here.
admin.site.register(Store)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Cart)
