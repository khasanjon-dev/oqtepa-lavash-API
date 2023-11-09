from orders.models import Order
from orders.serializers.order import OrderSerializer
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


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

    @action(methods=['get'], detail=True)
    def orders(self, request):
        """
        ```
        order lar listini olish uchun
        ```
        """
        orders = request.user.order_set
        orders_ids = orders.values_list('order', flat=True)
