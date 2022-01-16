from enum import unique
from unicodedata import category
from django.db import models
from django.forms import IntegerField
from accounts.models import Account, Customer

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50, unique=True)
    seller = models.ForeignKey(Account, on_delete=models.CASCADE)
    address = models.TextField()
    store_link = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Categories(models.Model):
    name = models.CharField(max_length=100)
    store = models.ForeignKey(Store, on_delete=models.CASCADE,related_name="categories")

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    mrp = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    product_image = models.ImageField(null = True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE,related_name="products")

    def __str__(self):
        return self.name

class Order(models.Model):
    buyer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    store = models.ForeignKey(Store, on_delete= models.PROTECT)
    date = models.DateTimeField(auto_now=True)
    total_value = models.IntegerField(default=0)

class Cart(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name="product")
    products = models.ForeignKey(Products, on_delete = models.PROTECT)
    quantity = models.IntegerField(default = 1)
    value = models.IntegerField(default = 0)
    
