from django.urls import include, path
from products.views.category import CategoryListAPIView
from products.views.product import ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductViewSet)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('', include(router.urls)),
]
