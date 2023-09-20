from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from users.serializers.jwt_auth import MyTokenObtainPairSerializer


class LoginView(TokenObtainPairView):
    """
    ## login qilish uchun
    ```
    {
        "phone": "901001010",
        "code": "2010"
    }
    ```
    """
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
