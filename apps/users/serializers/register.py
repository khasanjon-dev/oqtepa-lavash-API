import datetime
import re

from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, IntegerField
from rest_framework.generics import get_object_or_404
from rest_framework.serializers import Serializer

from users.models import User


def is_phone_number(phone: str):
    pattern = r'^(?:\+998|998|)([1-9]\d{8})$'
    match = re.match(pattern, phone)
    if match:
        return True
    else:
        return False


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
