from django.urls import include, path
from orders.views.order import OrderViewSet
from orders.views.orderItem import OrderItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', OrderViewSet)
router.register('item', OrderItemViewSet)
urlpatterns = [
    path('', include(router.urls))
]
