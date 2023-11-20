from products.models import Category
from products.serializers import CategorySerializer, ProductSerializer
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


class CategoryViewSet(ListModelMixin, GenericViewSet):
    """
    categoriyalar listini olish

    ```
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=['get'], detail=True, permission_classes=(IsAuthenticated,), serializer_class=ProductSerializer)
    def product(self, request, pk):
        """
        category id yuboriladi va shu categoriyaga tegishli barcha productlar qaytadi

        ```
        """
        pass
