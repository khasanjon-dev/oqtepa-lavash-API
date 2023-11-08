from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from orders.models import Order
from orders.serializers.order import OrderSerializer


class OrderViewSet(CreateModelMixin, GenericViewSet):
    """
    ## Example:
    ```
    {
        "address": "Toshkent, Chilonzor 6",
        "delivery_price": 10000,
        "total_price": 100000,
        "payment_method": "cash" or "click",
        "reception_type": "delivery" or "pickup"
    }
    ```
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)
