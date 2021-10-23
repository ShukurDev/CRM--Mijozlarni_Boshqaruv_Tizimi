import django_filters
from .models import Order
from django.db import models


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer']
