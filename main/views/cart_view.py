from users.models import User
from rest_framework import status
from django.db import IntegrityError
from main.models import CartItem, Cart
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from main.serializers import CartItemSerializer, CartItemUpdateSerializer, CartSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, get_object_or_404


class CartItemCreateAPIView(CreateAPIView):
    """
        Создание нового товара в корзине.

        Параметры:
        - `user_id`: Идентификатор пользователя, добавляющего товар.

        Поведение:
        - Пытается создать новый товар в корзине пользователя.
        - Если товар с таким идентификатором и продуктом уже существует, вызывает ошибку IntegrityError.
    """
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def perform_create(self, serializer):
        try:
            if serializer.is_valid():
                user_id = self.request.user.id
                cart_item = serializer.save(user_id=user_id)

                cart = Cart.objects.get(user_id=user_id)
                cart.items.add(cart_item)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            raise ValidationError('Такой товар уже есть в корзине пользователя.')


class CartItemUpdateAPIView(UpdateAPIView):
    """
        Обновление существующего товара в корзине.

        Поведение:
        - Получает список товаров корзины для текущего пользователя.
        - Позволяет обновить данные товара по его идентификатору пользователя.
    """
    serializer_class = CartItemUpdateSerializer

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)


class CartItemDeleteAPIView(DestroyAPIView):
    """
       Удаление товара из корзины.

       Поведение:
       - Получает список товаров корзины для текущего пользователя.
       - Позволяет удалить товар из корзины по его идентификатору.
    """
    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(
            {'success': 'Товар удален'},
            status=status.HTTP_204_NO_CONTENT
        )


class CartDetailAPIView(APIView):
    """
        Получение информации о корзине пользователя.

        Поведение:
        - Получает информацию о корзине для текущего пользователя.
        - Возвращает данные о корзине в виде сериализованного объекта.
    """
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        user = self.request.user
        queryset = Cart.objects.filter(user=user)
        print(user.id)

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClearCartItemsAPIView(APIView):
    """
        Очистка корзины пользователя.

        Поведение:
        - Получает пользователя по его идентификатору.
        - Получает корзину пользователя и удаляет из нее все товары.
    """
    @staticmethod
    def get(request, *args, **kwargs):
        user = User.objects.get(id=5)
        cart = get_object_or_404(Cart, user=user)

        cart.items.all().delete()

        return Response({'detail': 'Все товары в корзине удалены'}, status=status.HTTP_204_NO_CONTENT)
