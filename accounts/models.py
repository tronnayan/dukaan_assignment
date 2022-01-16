from django.db import models
# Create your models here.

class Account(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    otp = models.IntegerField(default=0)

    def __str__(self):
        return self.phone
 
class Customer(models.Model):
    phone = models.CharField(max_length=13, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.phone
