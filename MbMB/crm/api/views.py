from rest_framework import viewsets, generics
from ..models import *
from .serializers import CustomerSerializer, ProductSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.name:
            return None
        return ProductSerializer

    permission_classes = [IsAuthenticated, IsAdminUser]


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = OrderSerializer

