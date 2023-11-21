from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views.auth import CustomTokenRefreshView, LoginView
from users.views.user import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet, 'users')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh/', CustomTokenRefreshView.as_view(), name='refresh'),
    path('', include(router.urls))
]
