from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response
from stores.serializers import StoreSerializer
from .models import Account
from accounts.jwt import verify_token
from accounts.serializers import SellerSerializer
from rest_framework import generics

# Create your views here.
class SellerView(generics.CreateAPIView):
    serializer_class  = SellerSerializer

