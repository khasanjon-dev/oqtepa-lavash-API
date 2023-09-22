from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from orders.models import Order
from orders.serializers.order import OrderSerializer


class OrderViewSet(CreateModelMixin, GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
