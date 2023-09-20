from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import Serializer

from utils.validations import is_phone_number


class RegisterSerializer(Serializer):
    phone = CharField(max_length=9)
    name = CharField()

    def validate(self, attrs):
        phone = attrs.get('phone')
        if not is_phone_number(phone):
            raise ValidationError("Telefon raqam to'g'ri kiriting!")
        return attrs


class CodeCheckSerializer(Serializer):
    phone = CharField(max_length=9)
    code = IntegerField()

    def validate(self, attrs):
        phone = attrs.get('phone')
        code = attrs.get('code')
        if not is_phone_number(phone):
            raise ValidationError("Telefon raqam to'g'ri kiriting!")
        if not (cache.get(phone) and cache.get(phone) == code):
            raise ValidationError('Kod mos kelmadi!')
        else:
            cache.delete(phone)
        return attrs


class PhoneSerializer(Serializer):
    phone = CharField(max_length=9)

    def validate(self, attrs):
        phone = attrs.get('phone')
        if not is_phone_number(phone):
            raise ValidationError("Telefon raqam to'g'ri kiriting!")
        return attrs
