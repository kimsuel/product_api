from rest_framework import serializers

from api.models import Product, ShoppingCart


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ShoppingCartSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')

    class Meta:
        model = ShoppingCart
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'read_only': True},
        }


class ShoppingCartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ShoppingCartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = '__all__'
        extra_kwargs = {
            'user_id': {'read_only': True},
            'product': {'required': False},
            'quantity': {'required': False},
        }
