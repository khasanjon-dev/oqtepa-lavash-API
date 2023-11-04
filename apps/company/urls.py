from django.urls import path

from company.views import AboutListAPIView, PhoneListAPIView, SocialListAPIView, SettingsListAPIView, \
    LocationListAPIView

urlpatterns = [
    path('about/', AboutListAPIView.as_view(), name='about'),
    path('phone/', PhoneListAPIView.as_view(), name='phone'),
    path('social/', SocialListAPIView.as_view(), name='social'),
    path('settings/', SettingsListAPIView.as_view(), name='settings'),
    path('location/', LocationListAPIView.as_view(), name='location'),
]
