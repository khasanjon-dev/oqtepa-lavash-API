from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from orders.models import Order


class OrderSerializer(ModelSerializer):
    customer = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateAPIViewModelSerializer(ModelSerializer):
    customer = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Order
        fields = ('address', 'delivery_price', 'reception_type', 'customer')
