from django.urls import include, path
from rest_framework import routers
from rest_framework_nested import routers as nested_routers

from .apps import MainConfig
from .views.cart_view import CartItemViewSet, CartViewSet
from .views.category_view import CategoryListAPIView
from .views.product_view import ProductListAPIView

app_name = MainConfig.name

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('products/', ProductListAPIView.as_view(), name='products'),
]

router = routers.SimpleRouter()
router.register('carts', CartViewSet, 'carts')

nested_router = nested_routers.NestedSimpleRouter(router, r'carts', lookup='carts')
nested_router.register(r'items', CartItemViewSet, basename='carts-items')

urlpatterns += [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
