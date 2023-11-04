from rest_framework.serializers import ModelSerializer

from company.models import About, Phone, Social, Settings


class AboutModelSerializer(ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class PhoneModelSerializer(ModelSerializer):
    class Meta:
        model = Phone
        fields = '__all__'


class SocialModelSerializer(ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'


class SettingsModelSerializer(ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'
