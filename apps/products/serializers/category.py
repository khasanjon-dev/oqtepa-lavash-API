from rest_framework.serializers import ModelSerializer

from products.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'icon')
