from rest_framework import viewsets

from api.models import Product, ShoppingCart
from api.serializers import (
    ProductSerializer,
    ShoppingCartSerializer,
    ShoppingCartCreateSerializer,
    ShoppingCartUpdateSerializer
)
from configs.viewsets import MappingViewSetMixin


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShoppingCartViewSet(MappingViewSetMixin, viewsets.ModelViewSet):
    queryset = ShoppingCart.objects.all()
    serializer_class = ShoppingCartSerializer
    serializer_action_map = {
        'create': ShoppingCartCreateSerializer,
        'partial_update': ShoppingCartUpdateSerializer,
    }
    lookup_field = 'user_id'

    def get_queryset(self):
        return ShoppingCart.objects.filter(user_id=self.kwargs['user_id'])