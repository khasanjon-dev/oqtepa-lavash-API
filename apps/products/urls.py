from django.urls import path, include
from rest_framework.routers import DefaultRouter

from products.views.category import CategoryModelViewSet
from products.views.product import ProductModelViewSet

router = DefaultRouter()
router.register('', ProductModelViewSet)
router.register('category', CategoryModelViewSet)
urlpatterns = [
    path('', include(router.urls))
]
