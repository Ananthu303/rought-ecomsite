from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class audiomodel(models.Model):
    audioname = models.CharField(max_length=30)
    audioimage = models.ImageField(upload_to='djangoapp/static')
    audiofile = models.FileField(upload_to='djangoapp/static')


class shopregmodel(models.Model):
    shopname = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.IntegerField()
    def __str__(self):
        return self.shopname


class productuploadmodel(models.Model):
    shopid=models.IntegerField()
    pname = models.CharField(max_length=30)
    price = models.IntegerField()
    des = models.CharField(max_length=500)
    pimage = models.ImageField(upload_to='djangoapp/static')
    def __str__(self):
        return self.pname


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user


class cart(models.Model):
    username=models.CharField(max_length=30)
    pname = models.CharField(max_length=30)
    price = models.IntegerField()
    des = models.CharField(max_length=500)
    pimage = models.ImageField()
    def __str__(self):
        return self.pname


class wishlistm(models.Model):
    userid=models.IntegerField()
    pname = models.CharField(max_length=30)
    price = models.IntegerField()
    des = models.CharField(max_length=500)
    pimage = models.ImageField()
    def __str__(self):
        return self.pname


class buy(models.Model):
    pname = models.CharField(max_length=30)
    price = models.IntegerField()
    des = models.CharField(max_length=500)
    pimage = models.ImageField()
    quantity = models.IntegerField()
    def __str__(self):
        return self.pname



class customerdetailsmodel(models.Model):
    name = models.CharField(max_length=30)
    cardno = models.CharField(max_length=30)
    cardexpiry=models.CharField(max_length=30)
    security=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class shop_notification(models.Model):
    content=models.CharField(max_length=200)
    Datetimeshop=models.DateTimeField(auto_now_add=True)



class user_notification(models.Model):
    content=models.CharField(max_length=200)
    datetimeuser=models.DateTimeField(auto_now_add=True)
