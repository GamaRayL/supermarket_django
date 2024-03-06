from rest_framework.generics import ListAPIView
from main.models.category_model import Category
from rest_framework.permissions import AllowAny
from main.serializers.category_serializer import ListCategorySerializer


class CategoryListAPIView(ListAPIView):
    """Вывод списка категорий"""
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer
    permission_classes = [AllowAny]
