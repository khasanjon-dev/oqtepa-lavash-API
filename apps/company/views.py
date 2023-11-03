from rest_framework.generics import ListAPIView

from company.models import About, Phone
from company.serializers import AboutSerializer, PhoneSerializer


class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class PhoneListAPIView(ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
