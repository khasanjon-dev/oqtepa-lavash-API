from orders.models import OrderItem
from orders.serializers.orderItem import OrderItemSerializer
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class OrderItemViewSet(CreateModelMixin, GenericViewSet):
    """
    ### Order-Item Productlarni yaratish uchun
    ## Example:
    ```
    {
        "address": "Toshken Chilonzor 6",
        "delivery_price": 10000,
        "total_price": 50000,
        "status": "pending",
        "payment_method": "cash",
        "reception_type": "delivery"
    }
    ```
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=False)
    def order(self, request):
        """
        ## yaratilgan orderlar listini olish
        """
        queryset = OrderItem.objects.filter(order__customer=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
