from rest_framework.generics import ListAPIView

from products.models import Category
from products.serializers import CategorySerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
