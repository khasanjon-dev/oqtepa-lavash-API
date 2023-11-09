from orders.models import Order
from rest_framework.fields import CurrentUserDefault, HiddenField
from rest_framework.serializers import ModelSerializer


class OrderSerializer(ModelSerializer):
    customer = HiddenField(default=CurrentUserDefault())

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
        )
