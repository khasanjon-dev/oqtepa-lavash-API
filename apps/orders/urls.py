from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.views.order import OrderViewSet
from orders.views.orderItem import OrderItemViewSet

router = DefaultRouter()
router.register('order', OrderViewSet)
router.register('order-item', OrderItemViewSet)
urlpatterns = [
    path('', include(router.urls))
]
