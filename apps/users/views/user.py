from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import (AllowAny, IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from products.models import Product
from users.models import Favorite, User
from users.models.addition import Basket
from users.serializers import (CodeCheckSerializer, RegisterSerializer,
                               UserModelSerializer)
from users.serializers.addition import (BasketModelSerializer,
                                        FavoriteModelSerializer,
                                        NoneSerializer, ProductSerializer)
from users.serializers.register import PhoneSerializer
from users.serializers.user import UserProfileSerializer, UserSerializer
from utils.send_code import send_code_phone


class UserViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=RegisterSerializer)
    def register(self, request):
        """
        register qilish uchun

        ```
        "name": "Khasan",
        "phone": "901001010"
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.data.get('phone')
        name = serializer.data.get('name')
        user, created = User.objects.update_or_create(phone=phone)
        user.name = name
        user.save()
        code = send_code_phone(user.phone)
        data = serializer.data
        detail = 'update'
        if created:
            detail = 'create'
        data['message'] = detail
        data['code'] = code
        return Response(data)

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=PhoneSerializer,
            url_path='send-code')
    def send_code(self, request):
        """
        Sms yuborish uchun phone yuboriladi

        ```
        "phone": "901001010"
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

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=CodeCheckSerializer,
            url_path='change-phone')
    def change_phone(self, request):
        """
        raqamni o'zgartirish uchun

        ```
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

    @action(methods=['post'], detail=False, permission_classes=(AllowAny,), serializer_class=CodeCheckSerializer,
            url_path='check-code')
    def check_code(self, request):
        """
        yuborilgan sms ni tekshirish uchun

        ```
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
        user ma'lumotlarini yangilash uchun

        ```
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.filter(phone=request.user.phone).update(**serializer.data)
        detail = {
            'message': 'User yangilandi!'
        }
        return Response(detail)

    @action(methods=['get'], detail=False, permission_classes=(IsAuthenticated,), serializer_class=UserSerializer)
    def about(self, request):
        """
        user ma'lumotlarini olish uchun

        ```
        """

        serializer = self.serializer_class(request.user)
        return Response(serializer.data)

    # addition actions
    # ----------------------------------------------------------------------------------------------------------
    # addition actions

    @action(methods=['get'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=NoneSerializer)
    def favorite(self, request, pk):
        """
        sevimlilarga qo'shish va o'chirish

        ```
        """
        try:
            favorite, created = Favorite.objects.get_or_create(customer=request.user, product_id=pk)
            if not created:
                if favorite.is_like:
                    favorite.is_like = False
                else:
                    favorite.is_like = True
                favorite.save()
            serializer = FavoriteModelSerializer(favorite)
            return Response(serializer.data)
        except Exception as e:
            detail = {
                'message': "Sevimlilarga qo'shishda xatolik!",
                'error': f'{e}'
            }
            return Response(detail, status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=NoneSerializer,
            url_path='delete-favorite')
    def delete_favorite(self, request, pk):
        """
        sevimlilardan o'chirish

        ```
        """
        try:
            favorite = Favorite.objects.filter(customer=request.user, product_id=pk).update(is_like=False)
            serializer = FavoriteModelSerializer(favorite)
            return Response(serializer.data)
        except Exception as e:
            detail = {
                'message': "Sevimlilardan o'chirishda xatolik!",
                'error': f'{e}'
            }
            return Response(detail, status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, permission_classes=(IsAuthenticated,),
            serializer_class=ProductSerializer)
    def favorites(self, request):
        """
        favorite lar listini olish uchun

        ```
        """
        favorites = Favorite.objects.filter(customer=request.user, is_like=True)
        product_ids = favorites.values_list('product', flat=True)
        query = Product.objects.all()
        queryset = query.filter(id__in=product_ids)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=NoneSerializer)
    def basket(self, request, pk):
        """
        savatga qo'shish va +1 qo'shish uchun

        ```
        """
        try:
            basket, created = Basket.objects.get_or_create(customer=request.user, product_id=pk)
            serializer = BasketModelSerializer(basket)
            if created:
                return Response(serializer.data, status.HTTP_201_CREATED)
            basket.quantity += 1
            basket.save()
            return Response(serializer.data)
        except Exception as e:
            detail = {
                'message': "Savatga qo'shishda xatolik!",
                'exception': f'{e}'
            }
            return Response(detail, status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=NoneSerializer,
            url_path='delete-basket')
    def delete_basket(self, request, pk):
        """
        savatdan  o'chirish uchun -1 dan

        ```
        """
        basket = get_object_or_404(Basket, customer=request.user, id=pk)
        serializer = BasketModelSerializer(basket)
        if basket.quantity - 1 == 0:
            serializer.data['id'] = basket.id
            basket.delete()
            return Response(serializer.data)
        basket.quantity -= 1
        basket.save()
        return Response(serializer.data)

    @action(methods=['delete'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=NoneSerializer,
            url_path='remove-basket')
    def remove_basket(self, request, pk):
        """
        savatdan o'chirish yani shu productni o'chiradi qiladi

        ```
        """
        basket = get_object_or_404(Basket, customer=request.user, id=pk)
        serializer = BasketModelSerializer(basket)
        serializer.data['id'] = basket.id
        basket.delete()
        return Response(serializer.data)

    @action(methods=['get'], detail=False, permission_classes=(IsAuthenticated,),
            serializer_class=BasketModelSerializer, url_path='basket')
    def baskets(self, request):
        """
        savat dagi productlar listini olish

        ```
        """
        basket = request.user.basket
        queryset = basket
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
