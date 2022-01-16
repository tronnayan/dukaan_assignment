from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.db.models import Q, Count
from rest_framework.response import Response
from accounts.models import Customer
from stores.serializers import CartSerializer, CategorySerializer, OrderSerializer, ProductSerializer, StoreDetailSerializer, StoreSerializer
from .models import Account, Categories, Order, Products, Store
from accounts.jwt import verify_token

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

class StoreDetailView(APIView):
    def get(self, request, store_name):
        store = ' '.join(store_name.split("-"))
        store_obj = Store.objects.get(name = store)
        serializer = StoreDetailSerializer(store_obj, many = False)
        return Response(serializer.data)        

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
            request.data["category"] = category.id
            serializer = ProductSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response({"User Not Found": "Seller Not Registered"})


class OrderView(APIView):
    def post(self, request,store_name):
        store = ' '.join(store_name.split("-"))
        store_obj = Store.objects.get(name = store)
        token = request.headers["Authorization"]
        customer_num = verify_token(token)
        customer = Customer.objects.get(phone = customer_num)
        order = Order.objects.create(buyer = customer, store = store_obj)
        data = request.data

        for res in data:
            res["value"] = (Products.objects.get(id = res["products"]).sale_price) * res["quantity"]
            order.total_value += res["value"]
            res["order"] = order.id

        order.save()
        serializer = CartSerializer(data = data, many = True)
        if serializer.is_valid():
            serializer.save()

        oserializer = OrderSerializer(order, many = False)
        return Response(oserializer.data)
        
        

