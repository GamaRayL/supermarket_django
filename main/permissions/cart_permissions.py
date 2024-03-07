from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet

from ..models.cart_model import Cart


class CartActionsPermission(BasePermission):
    def has_permission(self, request: Request, view: GenericViewSet) -> bool:
        if view.action == 'retrieve':
            return getattr(request.user, 'cart', None) is not None
        return True

    def has_object_permission(
            self,
            request: Request,
            view: GenericViewSet,
            cart: Cart,
    ) -> bool:
        return request.user.pk == cart.user_id


class CartItemActionsPermission(BasePermission):
    def has_permission(self, request: Request, view: GenericViewSet) -> bool:
        if cart := getattr(request.user, 'cart', None):
            return cart.pk == int(view.kwargs['carts_pk'])
        return False
