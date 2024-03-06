from main.models.product_model import Product
from main.serializers.category_serializer import ListCategorySerializer
from rest_framework.serializers import ModelSerializer, Serializer, ImageField


class ImageSerializer(Serializer):
    """Сериализатор изображения для товара"""
    image_small = ImageField()
    image_medium = ImageField()
    image_large = ImageField()


class ProductSerializer(ModelSerializer):
    """Сериализатор товара"""
    images = ImageSerializer(source='*', read_only=True)
    category = ListCategorySerializer()

    class Meta:
        model = Product
        fields = ('name', 'slug', 'category', 'price', 'images')
