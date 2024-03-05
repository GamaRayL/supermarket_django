from main.models import Category
from rest_framework.permissions import AllowAny
from main.paginations import CategoryPagination
from rest_framework.generics import ListAPIView
from main.serializers import ListCategorySerializer


class CategoryListAPIView(ListAPIView):
    """Вывод списка категорий"""
    queryset = Category.objects.all()
    serializer_class = ListCategorySerializer
    pagination_class = CategoryPagination
    permission_classes = [AllowAny]
