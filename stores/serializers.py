from ast import Store
from dataclasses import field
from pickletools import read_long1
from .models import Store, Products, Categories, Order, Cart
from rest_framework import serializers
from accounts.jwt import create_access_token, verify_token

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store 
        fields = ('id','name','seller','address','store_link')
        extra_kwargs = {'name':{'write_only': True},"seller":{'write_only': True}, "address":{'write_only': True}}


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('id', 'name','description','mrp','sale_price','category','product_image')
        # extra_kwargs = {'description':{'write_only': True},"mrp":{'write_only': True}, "sale_price":{'write_only': True}}


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only = True, many = True)
    class Meta:
        model = Categories
        fields = ('id', 'name','store','products')

class StoreDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(read_only = True, many = True)
    class Meta:
        model = Store 
        fields = ('id','name','seller','address','store_link','categories')
        extra_kwargs = {"seller":{'write_only': True}}

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('order',"products","quantity","value")
        extra_kwargs = {"order":{"write_only": True}}

class OrderSerializer(serializers.ModelSerializer):
    product = CartSerializer(read_only = True, many = True)
    class Meta:
        model = Order
        fields = ('id','date','store','product','total_value')