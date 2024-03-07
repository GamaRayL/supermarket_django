from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .base import SerializerActionMixin
from ..models.cart_model import Cart, CartItem
from ..permissions.cart_permissions import (
    CartActionsPermission,
    CartItemActionsPermission,
)
from ..serializers.cart_serializer import (
    CartItemCreateSerializer,
    CartItemUpdateSerializer,
    CartCreateSerializer,
    CartRetrieveSerializer,
)


class CartViewSet(
    SerializerActionMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Cart.objects.all()
    serializer_class_create = CartCreateSerializer
    serializer_class_retrieve = CartRetrieveSerializer
    permission_classes = [IsAuthenticated, CartActionsPermission]

    @action(detail=True, methods=["delete"])
    def clear(self, request, *args, **kwargs):
        self.get_object().items.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartItemViewSet(
    SerializerActionMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class_create = CartItemCreateSerializer
    serializer_class_update = CartItemUpdateSerializer
    permission_classes = [IsAuthenticated, CartItemActionsPermission]

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.kwargs['carts_pk'])
