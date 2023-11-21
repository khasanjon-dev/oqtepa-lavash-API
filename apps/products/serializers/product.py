from rest_framework.fields import BooleanField
from rest_framework.serializers import ModelSerializer

from products.models import Product


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
            rep['is_like'] = instance.favorites.filter(customer=request.user).exists()
        return rep

