from products.models import Product
from rest_framework.serializers import ModelSerializer, Serializer
from users.models import Favorite
from users.models.addition import Basket


class NoneSerializer(Serializer):
    pass


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'category_id')


class BasketModelSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Basket
        fields = ('id', 'quantity', 'product')


class FavoriteModelSerializer(ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Favorite
        fields = (
            'id',
            'product',
        )
