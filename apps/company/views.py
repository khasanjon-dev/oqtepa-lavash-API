from company.models import About, Location, Phone, Region, Settings, Social
from company.serializers import (AboutModelSerializer, LocationModelSerializer,
                                 PhoneModelSerializer, RegionModelSerializer,
                                 SettingsModelSerializer,
                                 SocialModelSerializer)
from rest_framework.generics import ListAPIView


class AboutListAPIView(ListAPIView):
    """
    kompaniya haqidagi ma'lumotlarni olish

    ```
    """
    queryset = About.objects.all()
    serializer_class = AboutModelSerializer


class PhoneListAPIView(ListAPIView):
    """
    telefon raqamlar listi

    ```
    """
    queryset = Phone.objects.all()
    serializer_class = PhoneModelSerializer


class SocialListAPIView(ListAPIView):
    """
    social linklar listi

    ```
    """
    queryset = Social.objects.all()
    serializer_class = SocialModelSerializer


class SettingsListAPIView(ListAPIView):
    """
    default bo'lgan narsalar listi

    ```
    """
    queryset = Settings.objects.all()
    serializer_class = SettingsModelSerializer


class LocationListAPIView(ListAPIView):
    """
    manzillar listi

    ```
    """
    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer


class RegionListAPIView(ListAPIView):
    """
    region lar listi

    ```
    """
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
