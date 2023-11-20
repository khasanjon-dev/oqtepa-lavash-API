from django.urls import include, path
from products.views.category import CategoryViewSet
from products.views.product import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
