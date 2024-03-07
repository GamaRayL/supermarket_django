from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from users.models import User
from .base import CurrentUserCart
from ..models.cart_model import Cart, CartItem
from ..models.product_model import Product


class CartItemSerializer(ModelSerializer):
    """Сериалайзер товара"""
    product = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        fields = ('id', 'product')
        model = CartItem


class CartItemCreateSerializer(ModelSerializer):
    """Сериалайзер создания товара"""
    cart = serializers.PrimaryKeyRelatedField(
        queryset=Cart.objects.all(),
        default=CurrentUserCart(),
    )
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
    )

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'cart')


class CartItemUpdateSerializer(ModelSerializer):
    """Сериалайзер обновления товара"""
    quantity = serializers.IntegerField(required=True)

    class Meta:
        model = CartItem
        fields = ('quantity',)


class CartRetrieveSerializer(ModelSerializer):
    """Сериалайзер просмотра корзины"""
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'total_price', 'total_quantity', 'items')


class CartCreateSerializer(ModelSerializer):
    """Сериалайзер создания корзины"""
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    
    class Meta:
        model = Cart
        fields = ('id', 'user')

    @staticmethod
    def validate_user(user: User) -> User:
        if getattr(user, 'cart', None):
            raise serializers.ValidationError(
                f'У этого пользователя уже есть корзина: {user.cart}'
            )
        return user
