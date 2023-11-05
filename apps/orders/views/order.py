from rest_framework.generics import CreateAPIView

from orders.models import Order
from orders.serializers.order import OrderCreateAPIViewModelSerializer


class OrderCreateAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateAPIViewModelSerializer
