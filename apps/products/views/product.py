from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from products.filter import ProductFilterSet
from products.models import Product
from products.serializers import ProductSerializer
from products.serializers.product import BasketModelSerializer, NoneSerializer
from users.models import Favorite
from users.models.addition import Basket


class ProductViewSet(ListModelMixin, GenericViewSet):
    """
    ```
    category id yuboriladi va shu categoriyaga tegishli barcha productlar qaytadi
    id yuborilmasa barcha productlar listi qaytadi
    ```
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilterSet

    @action(methods=['get'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=NoneSerializer,
            url_path='add-favorite')
    def add_favorite(self, request, pk):
        """
        sevimlilarga qo'shish
        """
        try:
            favorite, created = Favorite.objects.get_or_create(customer=request.user, product_id=pk)
            detail = {'success': True}
            if created:
                return Response(detail, status.HTTP_201_CREATED)
            detail['message'] = 'Already added!'
            return Response(detail)
        except Exception as e:
            print(e)
            detail = {'message': "Sevimlilarga qo'shishda xatolik!"}
            return Response(detail, status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=NoneSerializer,
            url_path='delete-favorite', filter_backends=None)
    def delete_favorite(self, request, pk):
        """
        sevimlilardan o'chirish
        """
        try:
            Favorite.objects.filter(customer=request.user, product_id=pk).delete()
            detail = {
                'success': True
            }
            return Response(detail, 204)
        except Exception as e:
            print(e)
            detail = {'message': "Sevimlilardan o'chirishda xatolik!"}
            return Response(detail, status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, permission_classes=(IsAuthenticated,), serializer_class=ProductSerializer,
            url_path='favorites')
    def favorites(self, request):
        """
        ```
        favorite lar listini olish uchun
        ```
        """
        favorites = request.user.favorites
        favorites_ids = favorites.values_list('product', flat=True)
        query = self.get_queryset()
        queryset = query.filter(id__in=favorites_ids)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=NoneSerializer)
    def basket(self, request, pk):
        """
        ```
        savatga qo'shish va update qilish uchun

        ```
        """
        try:
            basket, created = Basket.objects.get_or_create(customer=request.user, product_id=pk)
            detail = {
                'success': True,
                'quantity': basket.quantity,
                'product_id': basket.product_id,
                'message': 'Add basket!'
            }
            if created:
                return Response(detail, status.HTTP_201_CREATED)
            detail['message'] = 'Update basket!'
            basket.quantity += 1
            basket.save()
            detail['quantity'] = basket.quantity
            return Response(detail)
        except Exception as e:
            print(e)
            detail = {'message': "Savatga qo'shishda xatolik!"}
            return Response(detail, status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=NoneSerializer,
            url_path='delete-basket')
    def delete_basket(self, request, pk):
        """
        ```
        savatdan  o'chirish uchun -1 dan

        ```
        """
        basket = get_object_or_404(Basket, customer=request.user, id=pk)
        try:
            detail = {'product_id': basket.product_id}
            if basket.quantity - 1 == 0:
                basket.delete()
                detail.update(
                    {
                        'success': True,
                        'quantity': 0
                    }
                )
                return Response(detail, status.HTTP_204_NO_CONTENT)
            else:
                basket.quantity -= 1
                basket.save()
                detail.update(
                    {
                        'success': True,
                        'quantity': basket.quantity
                    }
                )
                return Response(detail, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            detail = {
                'message': "Savatdan o'chirishda xatolik!",
                'exception': f'{e}'
            }
            return Response(detail, status.HTTP_400_BAD_REQUEST)

    @action(methods=['delete'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=NoneSerializer,
            url_path='remove-basket')
    def remove_basket(self, request, pk):
        """
        ```
        savatdan  o'chirish  hammasini o'chiradi

        ```
        """
        basket = get_object_or_404(Basket, customer=request.user, id=pk)
        try:
            basket.delete()
            detail = {
                'success': True,
            }
            return Response(detail, status.HTTP_204_NO_CONTENT)
        except Exception as e:
            detail = {
                'message': "O'chirishda xatolik!",
                'detail': f'{e}'
            }
            return Response(detail, status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False, permission_classes=(IsAuthenticated,),
            serializer_class=BasketModelSerializer, url_path='basket')
    def baskets(self, request):
        """
        ```
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
