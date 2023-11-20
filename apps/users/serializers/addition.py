from rest_framework.serializers import Serializer, ModelSerializer

from products.models import Product
from users.models.addition import Basket


class NoneSerializer(Serializer):
    pass


class ProductSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'image', 'category_id')
        model = Product


class BasketModelSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ('id', 'quantity', 'product')
