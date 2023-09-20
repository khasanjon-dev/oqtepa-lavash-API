from rest_framework.serializers import ModelSerializer

from users.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'phone')


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'birth_date')


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'phone', 'birth_date', 'updated_at', 'created_at')
