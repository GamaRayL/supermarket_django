from main.models.category_model import Category
from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField


class BasicCategorySerializer(ModelSerializer):
    """Базовый сериалайзер для категории"""
    class Meta:
        model = Category
        fields = '__all__'


class ListCategorySerializer(ModelSerializer):
    """Сериалайзер списка категорий"""
    parent_category = SerializerMethodField()

    def get_parent_category(self, obj):
        """Метод для получения родительской категории"""
        return self.get_recursive_category(obj.parent_category) if obj.parent_category else None

    def get_recursive_category(self, category):
        """Метод для получения категорий рекурсивным способом"""
        serializer = BasicCategorySerializer(category)
        data = serializer.data

        if category.parent_category:
            data['parent_category'] = self.get_recursive_category(category.parent_category)

        return data

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'image', 'parent_category')
