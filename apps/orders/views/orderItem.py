from orders.models import OrderItem
from orders.serializers.orderItem import OrderItemSerializer
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


class OrderItemViewSet(CreateModelMixin, GenericViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)
