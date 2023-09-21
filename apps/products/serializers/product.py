from rest_framework.serializers import ModelSerializer, Serializer

from products.models import Product
from users.models import Favorite


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category_id')


class NoneSerializer(Serializer):
    pass
