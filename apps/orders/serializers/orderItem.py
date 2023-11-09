from rest_framework.serializers import ModelSerializer

from orders.models import OrderItem


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemsModelSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
