from rest_framework import serializers
from ..models import *


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    # name = serializers.CharField(max_length=200)
    # prise = serializers.DecimalField(max_digits=5, decimal_places=3)
    # category = serializers.CharField(max_length=1000)
    # description = serializers.CharField(max_length=500)
    # tags = serializers.CharField(max_length=100)
    # date = serializers.DateTimeField()
    #
    # def create(self, validated_data):
    #     return validated_data
    #
    # def update(self, instance, validated_data):
    #     return instance


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
