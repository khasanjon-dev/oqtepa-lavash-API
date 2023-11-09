from company.views import (AboutListAPIView, LocationListAPIView,
                           PhoneListAPIView, RegionListAPIView,
                           SettingsListAPIView, SocialListAPIView)
from django.urls import path

urlpatterns = [
    path('about/', AboutListAPIView.as_view(), name='about'),
    path('phone/', PhoneListAPIView.as_view(), name='phone'),
    path('social/', SocialListAPIView.as_view(), name='social'),
    path('settings/', SettingsListAPIView.as_view(), name='settings'),
    path('location/', LocationListAPIView.as_view(), name='location'),
    path('region/', RegionListAPIView.as_view(), name='region'),
]
