from django.urls import path

from company.views import AboutListAPIView

urlpatterns = [
    path('about/', AboutListAPIView.as_view(), name='about'),
]
