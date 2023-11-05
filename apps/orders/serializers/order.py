from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from orders.models import Order
from orders.serializers.orderItem import OrderItemSerializer


class OrderSerializer(ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    customer = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Order
        fields = '__all__'
