from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from orders.models import OrderItem
from orders.serializers.orderItem import OrderItemSerializer


class OrderItemViewSet(CreateModelMixin, GenericViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)

    # @action(methods=['get'], detail=True)
    # def orders(self, request):
    #     """
    #     ```
    #     order lar listini olish uchun
    #     ```
    #     """
    #     orders = request.user.order_set
    #     orders_ids = orders.values_list('order', flat=True)
