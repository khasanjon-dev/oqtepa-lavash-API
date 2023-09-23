from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from orders.models import OrderItem
from orders.serializers.orderItem import OrderItemSerializer


class OrderViewSet(CreateModelMixin, GenericViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
