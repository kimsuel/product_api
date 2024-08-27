from rest_framework import viewsets

from api.models import Product, ShoppingCart
from api.serializers import (
    ProductSerializer,
    ShoppingCartSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShoppingCartViewSet(viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
