from rest_framework.serializers import ModelSerializer

from company.models import About, Phone, Social, Settings, Branch, Location, Region


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


class BranchModelSerializer(ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class LocationModelSerializer(ModelSerializer):
    branch = BranchModelSerializer(required=True)

    class Meta:
        model = Location
        fields = '__all__'


class RegionModelSerializer(ModelSerializer):
    class Meta:
        model = Region
        fields = ('name',)
