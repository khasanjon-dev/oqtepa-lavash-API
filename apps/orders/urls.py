from django.urls import path

from orders.views.order import OrderCreateAPIView

urlpatterns = [
    path('create/', OrderCreateAPIView.as_view(), name='order')
]
