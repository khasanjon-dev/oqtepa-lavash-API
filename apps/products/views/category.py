from products.models import Category
from products.serializers import CategorySerializer
from rest_framework.generics import ListAPIView


class CategoryListAPIView(ListAPIView):
    """
    ```
    categoriyalar listini olish
    ```
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
