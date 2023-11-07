from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.views.order import OrderViewSet
from orders.views.orderItem import OrderItemViewSet

router = DefaultRouter()
router.register('', OrderViewSet)
router.register('item', OrderItemViewSet)
urlpatterns = [
    path('', include(router.urls))
]
