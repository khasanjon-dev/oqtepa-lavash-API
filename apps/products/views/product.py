from products.models import Product
from products.serializers.product import ProductModelSerializer
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet


class ProductViewSet(ListModelMixin, GenericViewSet):
    """
    productlar listini olish

    ```
    """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
