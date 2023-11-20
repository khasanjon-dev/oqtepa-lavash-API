from rest_framework.fields import BooleanField
from rest_framework.serializers import ModelSerializer, Serializer

from products.models import Product
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


class ProductModelSerializer(ModelSerializer):
    is_like = BooleanField(default=False, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'image',
            'category_id',
            'is_like'
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context['request']
        if request.user.is_authenticated:
            rep['is_like'] = instance.basket.filter(user=request.user).exists()
        return rep
