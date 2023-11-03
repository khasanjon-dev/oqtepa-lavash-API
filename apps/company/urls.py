from django.urls import path

from company.views import AboutListAPIView, PhoneListAPIView

urlpatterns = [
    path('about/', AboutListAPIView.as_view(), name='about'),
    path('phone/', PhoneListAPIView.as_view(), name='phone'),
]
