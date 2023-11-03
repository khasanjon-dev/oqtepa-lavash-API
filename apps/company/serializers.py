from rest_framework.serializers import ModelSerializer

from company.models import About, Phone


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = ('phone',)
