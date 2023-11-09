from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from users.views.auth import LoginView
from users.views.user import UserModelViewSet

router = DefaultRouter()
router.register('', UserModelViewSet, 'users')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('', include(router.urls))
]
