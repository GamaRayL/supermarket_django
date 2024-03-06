from main.models.product_model import Product
from rest_framework.generics import ListAPIView
from main.serializers.product_serializer import ProductSerializer



class ProductListAPIView(ListAPIView):
    """Вывод списка продуктов"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
