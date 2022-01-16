from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Account(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    otp = models.IntegerField(default=0)
 
class Customer(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    address = models.TextField()
