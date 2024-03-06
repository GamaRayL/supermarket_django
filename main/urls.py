from django.urls import path
from main.apps import MainConfig
from main.views.cart_view import (
    CartItemCreateAPIView,
    CartItemUpdateAPIView,
    CartItemDeleteAPIView,
    CartDetailAPIView,
    ClearCartItemsAPIView
)
from main.views.product_view import ProductListAPIView
from main.views.category_view import CategoryListAPIView

app_name = MainConfig.name

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    # Product эндпоинты
    path('products/', ProductListAPIView.as_view(), name='products'),
    # CartItem эндпоинты
    path('cart_item/create/', CartItemCreateAPIView.as_view(), name='create_cart_item'),
    path('cart_item/update/<int:pk>/', CartItemUpdateAPIView.as_view(), name='update_cart_item'),
    path('cart_item/delete/<int:pk>/', CartItemDeleteAPIView.as_view(), name='delete_cart_item'),
    # Cart эндпоинты
    path('cart/', CartDetailAPIView.as_view(), name='cart'),
    path('cart/clear/', ClearCartItemsAPIView.as_view(), name='clear_cart')
]
