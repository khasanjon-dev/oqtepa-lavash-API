from orders.models import Order
from orders.serializers.order import OrderSerializer
from orders.utils.pagination import CustomPageNumberPagination
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class OrderViewSet(CreateModelMixin, GenericViewSet):
    """
    ### Order yaratish uchun
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
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=False, serializer_class=OrderSerializer,
            pagination_class=CustomPageNumberPagination, )
    def orders(self, request):
        """
        ```
        Userga tegishli orderlar listini olish
        ```
        """
        orders = request.user.orders

        order_ids = orders.values_list('id', flat=True)
        query = self.get_queryset()
        queryset = query.filter(id__in=order_ids)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
