from main.models import Product
from main.paginations import ProductPagination
from main.serializers import ProductSerializer
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView


class ProductListAPIView(ListAPIView):
    """Вывод списка продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    permission_classes = [AllowAny]
