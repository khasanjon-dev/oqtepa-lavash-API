from rest_framework import status
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from users.addition import send_code
from users.models import User
from users.serializers import UserModelSerializer, RegisterSerializer, CodeCheckSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=RegisterSerializer)
    def register(self, request):
        """
        ### sms yuborish uchun phone raqam yuboriladi hamda ismi
        ```
        {
            "phone": "901001010"
            "name" "John"
        }
        ```
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data.get('phone', None)
        name = serializer.data.get('name')
        user = User.objects.filter(phone=phone)
        if User.objects.filter(phone=phone).exists():
            user = user.first()
            user.name = name
            user.save()
            send_code(user.phone)
            detail = {
                'message': 'Sms yuborildi!'
            }
            return Response(detail)
        user = User.objects.create({'phone': phone, 'name': name})
        send_code(user.phone)
        detail = {
            'message': 'Sms yuborildi!'
        }
        return Response(detail, status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=CodeCheckSerializer)
    def check(self, request):
        """
        ## yuborilgan code ni tekshirish
        ```
        {
            "phone": "901001010",
            "code": "2010"
        }
        ```
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.update(phone=serializer.data.get('phone'))
        detail = {
            "message": "Muvaffaqiyatli tekshirildi!"
        }
        return Response(detail)
