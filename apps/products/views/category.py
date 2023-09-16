from rest_framework.viewsets import ModelViewSet

from products.models import Category
from products.serializers.category import CategorySerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
