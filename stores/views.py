from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from stores.serializers import CategorySerializer, ProductSerializer, StoreSerializer
from .models import Account, Categories, Store
from accounts.jwt import verify_token
from accounts.serializers import SellerSerializer
from rest_framework import generics

# Create your views here.

class StoreView(APIView):
    def post(self, request):
        token = request.headers["Authorization"]
        seller_num = verify_token(token)
        if Account.objects.filter(phone = seller_num).exists():
            seller = Account.objects.get(phone = seller_num)
            store_link = "127.0.0.1:8000/store/"+str('-'.join(request.data.get("name").split(" ")))
            data = {
                "name" : request.data.get("name"),
                "seller" : seller.id,
                "address" : request.data.get("address"),
                "store_link" : store_link

            }
            serializer = StoreSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({"User Not Found": "Seller Not Registered"})

class ProductView(APIView):
    def post(self, request):
        token = request.headers["Authorization"]
        seller_num = verify_token(token)
        if Account.objects.filter(phone = seller_num).exists():
            seller = Account.objects.get(phone = seller_num)
            st = request.data.get("store")
            store = Store.objects.get(id = st)
            category_name = request.data.get("category")
            
            if Categories.objects.filter(Q(store = store) & Q(name = category_name)).exists():
                pass 
            else:
                cat_data = {
                            "name" : category_name,
                            "store" : store.id
                        }
                cat_serializer = CategorySerializer(data = cat_data)
                if cat_serializer.is_valid():
                    cat_serializer.save()
                else:
                    return Response(cat_serializer.errors)

            category = Categories.objects.get(Q(store = store) & Q(name = category_name))
            data = {
                "name" : request.data.get("name"),
                "description": request.data.get("description"),
                "mrp" : request.data.get("mrp"),
                "sale_price": request.data.get("sale_price"),
                "category": category.id
            }
            serializer = ProductSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response({"User Not Found": "Seller Not Registered"})



