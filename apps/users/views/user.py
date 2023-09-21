from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import User
from users.serializers import UserModelSerializer, CodeCheckSerializer
from users.serializers.register import PhoneSerializer
from users.serializers.user import UserProfileSerializer, UserSerializer
from utils.send_code import send_code_phone


class UserModelViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=PhoneSerializer)
    def send_code(self, request):
        """
        ## Sms yuborish uchun phone yuboriladi
        ```
        {
            "phone": "901001010"
        }
        ```
        --------------------------------------------------------------------------
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data.get('phone')
        user, created = User.objects.update_or_create(phone=phone)
        send_code_phone(user.phone)
        detail = {
            'message': 'Sms yuborildi!'
        }
        return Response(detail)

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=CodeCheckSerializer)
    def change_phone(self, request):
        """
        ## bundan avval
        1. /send_code/ sms yuboriladi
        yangi raqam va sms code yuboriladi
        ```
        {
            "phone": "901001010",
            "code": "2010"
        }
        ```
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data.get('phone')
        if User.objects.filter(phone=phone).exists():
            detail = {
                'message': 'Bunday raqam mavjud!'
            }
            return Response(detail, status.HTTP_400_BAD_REQUEST)
        User.objects.filter(phone=request.user.phone).update(phone=phone)
        detail = {
            'message': 'Telefon raqam yangilandi!'
        }
        return Response(detail)

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=CodeCheckSerializer)
    def check_code(self, request):
        """
        ## bundan avval
        1. /send_code/ sms yuboriladi
        yangi raqam va sms code yuboriladi
        ```
        {
            "phone": "901001010",
            "code": "2010"
        }
        ```
        """

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        detail = {
            'message': 'Muvaffaqiyatli tekshirildi!'
        }
        return Response(detail)

    @action(methods=['put'], detail=False, permission_classes=(IsAuthenticated,),
            serializer_class=UserProfileSerializer)
    def profile(self, request):
        """
        ### user ma'lumotlarini yangilash uchun
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.filter(phone=request.user.phone).update(**serializer.data)
        detail = {
            'message': 'User yangilandi!'
        }
        return Response(detail)

    @action(methods=['get'], detail=False, permission_classes=(IsAuthenticated,), serializer_class=UserSerializer)
    def me(self, request):
        """
        ```
        user ma'lumotlarini olish uchun
        ```
        """

        serializer = self.serializer_class(request.user)
        return Response(serializer.data)
