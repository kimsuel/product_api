from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import ProductViewSet, ShoppingCartViewSet

router = DefaultRouter(trailing_slash=False)
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
                  path('shopping-carts', ShoppingCartViewSet.as_view({'post': 'create'})),
                  path('shopping-carts/<uuid:user_id>', ShoppingCartViewSet.as_view({'get': 'retrieve',
                                                                                     'patch': 'partial_update',
                                                                                     'delete': 'destroy'})),
              ] + router.urls
