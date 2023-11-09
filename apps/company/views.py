from company.models import About, Location, Phone, Region, Settings, Social
from company.serializers import (AboutModelSerializer, LocationModelSerializer,
                                 PhoneModelSerializer, RegionModelSerializer,
                                 SettingsModelSerializer,
                                 SocialModelSerializer)
from rest_framework.generics import ListAPIView


class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutModelSerializer


class PhoneListAPIView(ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneModelSerializer


class SocialListAPIView(ListAPIView):
    queryset = Social.objects.all()
    serializer_class = SocialModelSerializer


class SettingsListAPIView(ListAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsModelSerializer


class LocationListAPIView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationModelSerializer


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionModelSerializer
