from main.models.cart_model import CartItem, Cart
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer


class CartItemUpdateSerializer(ModelSerializer):
    """Сериалайзер обновления товара"""
    class Meta:
        model = CartItem
        fields = ('quantity',)


class BaseCartItemSerializer(ModelSerializer):
    """Базовый сериалайзер товара"""
    product = SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = CartItem
        exclude = ('user',)


class CartItemSerializer(ModelSerializer):
    """Сериалайзер товара"""
    class Meta:
        model = CartItem
        fields = ('id', 'product')


class CartSerializer(ModelSerializer):
    """Сериалайзер корзины"""
    items = BaseCartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'total_price', 'total_quantity', 'items')
