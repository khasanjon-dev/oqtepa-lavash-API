from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from orders.serializers import OrderSerializer


# class OrderViewSet(CreateModelMixin, GenericViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     permission_classes = (IsAuthenticated,)

    # @action(methods=['get'], detail=False, permission_classes=(IsAuthenticated,))
    # def create_order(self, request):
    #     """
    #     order yaratish
    #     """
    #     try:
    #         Order.objects.get_or_create(customer=request.user, order_address=)
