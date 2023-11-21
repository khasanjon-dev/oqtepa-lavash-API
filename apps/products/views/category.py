from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from products.models import Category
from products.serializers.category import CategorySerializer
from products.serializers.product import ProductModelSerializer


class CategoryViewSet(ListModelMixin, GenericViewSet):
    """
    categoriyalar listini olish

    ```
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(methods=['get'], detail=True, serializer_class=ProductModelSerializer)
    def product(self, request, pk):
        """
        category id yuboriladi va shu categoriyaga tegishli barcha productlar qaytadi

        ```
        """
        category = get_object_or_404(Category, id=pk)
        products = category.products  # noqa
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
