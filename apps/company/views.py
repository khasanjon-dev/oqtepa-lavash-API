from rest_framework.generics import ListAPIView

from company.models import About
from company.serializers import AboutSerializer


class AboutListAPIView(ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
