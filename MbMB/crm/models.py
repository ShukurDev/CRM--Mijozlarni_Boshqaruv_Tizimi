from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('ichki mahsulot', 'Ichki mahsulot'),
        ('Tashqi mahsulot', 'Tashqi mahsulot'),
    )
    name = models.CharField(max_length=100)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, choices=CATEGORY)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    note = models.CharField(max_length=100, null=True)
    STATUS = (
        ('Navbatdagi', 'Navbatdagi'),
        ('Yetkazib berilyapdi', 'Yetkazib berilyapti'),
        ('Yetkazib berildi', 'Yetkazib berildi'),
    )
    status = models.CharField(max_length=200, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
