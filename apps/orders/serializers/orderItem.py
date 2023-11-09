from orders.models import OrderItem
from rest_framework.serializers import ModelSerializer


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemsModelSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
