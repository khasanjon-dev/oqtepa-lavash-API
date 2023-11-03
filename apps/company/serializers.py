from rest_framework.serializers import ModelSerializer

from company.models import About, Phone


class AboutSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        ref_name = 'AboutSerializer'


class PhoneSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'
        ref_name = 'PhoneSerializer'
