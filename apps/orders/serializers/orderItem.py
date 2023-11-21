from orders.models import OrderItem
from rest_framework.serializers import ModelSerializer
from users.serializers.addition import ProductSerializer


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemsModelSerializer(ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'
