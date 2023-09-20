from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views.category import CategoryListAPIView
from products.views.product import ProductViewSet

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('', include(router.urls)),
]
