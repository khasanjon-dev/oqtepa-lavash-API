from django.urls import path

from products.views.category import CategoryListAPIView
from products.views.product import ProductListAPIView

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product'),
    path('category/', CategoryListAPIView.as_view(), name='category')
]
