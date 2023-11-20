from products.models import Product
from rest_framework.serializers import ModelSerializer, Serializer
from users.models.addition import Basket


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category_id')


class NoneSerializer(Serializer):
    pass


class BasketModelSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ('id', 'quantity', 'product')
