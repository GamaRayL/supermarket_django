from users.views import (
    UserListAPIView,
    UserCreateAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
)
from django.urls import path
from users.apps import UsersConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    # User эндпоинты
    path('', UserListAPIView.as_view(), name='user_list'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='user_delete'),
    # Token эндпоинты
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
