from rest_framework.routers import DefaultRouter

from api.views import ProductViewSet, ShoppingCartsViewSet


router = DefaultRouter(trailing_slash=False)
router.register('products', ProductViewSet, basename='products')
router.register('shopping-carts', ShoppingCartsViewSet, basename='shopping-carts')

urlpatterns = [] + router.urls
