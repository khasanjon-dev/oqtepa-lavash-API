from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from orders.models import OrderItem
from orders.serializers.orderItem import OrderItemSerializer


class OrderItemViewSet(CreateModelMixin, GenericViewSet):
    """
    # bundan avval order yaratiladi va undan qaytgan order id order field ga yoziladi
    ### Order-Item Productlarni yaratish uchun
    ## Example:
    ```
    {
        "quantity": 1,
        "price": 10000,
        "order": 5,
        "product": 1
    }
    ```
    """
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'], detail=False)
    def order(self, request):
        """
        ## Userga tegishli order-item larni olish uchun orderlar listini olish
        """
        queryset = OrderItem.objects.filter(order__customer=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
