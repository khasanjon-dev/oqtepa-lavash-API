from rest_framework.generics import ListAPIView

from company.models import About, Phone, Social, Settings
from company.serializers import AboutModelSerializer, PhoneModelSerializer, SocialModelSerializer, \
    SettingsModelSerializer


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
