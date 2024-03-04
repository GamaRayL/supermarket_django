from users.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """Сериалайзер пользователя"""
    class Meta:
        model = User
        fields = '__all__'
