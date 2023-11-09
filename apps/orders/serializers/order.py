from rest_framework.fields import CurrentUserDefault, HiddenField
from rest_framework.serializers import ModelSerializer

from orders.models import Order
from orders.serializers.orderItem import OrderItemsModelSerializer


class OrderSerializer(ModelSerializer):
    customer = HiddenField(default=CurrentUserDefault())
    order_items = OrderItemsModelSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'id',
            'address',
            'delivery_price',
            'total_price',
            'created_date',
            'status',
            'reception_type',
            'customer',
            'order_items',
        )
