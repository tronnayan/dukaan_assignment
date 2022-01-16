from ast import Store
from dataclasses import field
from .models import Store, Products, Categories, Order, Cart
from rest_framework import serializers
from accounts.jwt import create_access_token, verify_token

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store 
        fields = ('id','name','seller','address','store_link')
        extra_kwargs = {'name':{'write_only': True},"seller":{'write_only': True}, "address":{'write_only': True}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('id', 'name','store')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name','description','mrp','sale_price','category')
        extra_kwargs = {'description':{'write_only': True},"mrp":{'write_only': True}, "sale_price":{'write_only': True}}

