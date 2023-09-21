from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from products.filter import ProductFilterSet
from products.models import Product
from products.serializers import ProductSerializer
from products.serializers.product import NoneSerializer
from users.models import Favorite


class ProductViewSet(ListModelMixin, GenericViewSet):
    """
    ```
    category id yuboriladi va shu categoriyaga tegishli barcha productlar qaytadi
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
            url_path='delete-favorite')
    def delete_favorite(self, request, pk):
        """
        sevimlilardan o'chirish
        """
        try:
            Favorite.objects.filter(customer=request.user, product_id=pk).delete()
            return Response({'success': True}, 204)
        except Exception as e:
            print(e)
            detail = {'message': "Sevimlilardan o'chirishda xatolik!"}
            return Response(detail, status.HTTP_400_BAD_REQUEST)
