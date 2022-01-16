from ast import Store
from dataclasses import field
from .models import Account, Customer
from rest_framework import serializers
from accounts.jwt import create_access_token, verify_token
import random

class SellerSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = Account 
        fields = ('id','phone','otp','token')
        extra_kwargs = {'phone': {'write_only': True}, 'otp': {'write_only': True}}
    
    def create(self,validated_data):
        OTP = random.randint(1000,9999)
        seller = Account.objects.create(
            phone = validated_data["phone"],
            otp = OTP
        )
        seller.save()
        return (seller)
    
    def get_token(self,account_obj):
        tok = create_access_token(data = {"sub":account_obj.phone})
        return tok

