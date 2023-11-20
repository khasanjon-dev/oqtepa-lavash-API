from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase

from users.serializers.jwt_auth import MyTokenObtainPairSerializer


class LoginView(TokenObtainPairView):
    """
    access va refresh token olish uchun

    ```
    1. bundan avval register ga yuboriladi
    ```
    ```
    {
        "phone": "901001010",
        "code": "2010",
    }
    ```
    """
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class CustomTokenRefreshView(TokenViewBase):
    """
    refresh token olish uchun

    ```
    """

    _serializer_class = api_settings.TOKEN_REFRESH_SERIALIZER
