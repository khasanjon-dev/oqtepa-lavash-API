from random import randint

from django.core.cache import cache

from root.settings import REDIS_TIMEOUT


def generate_code():
    code = randint(1000, 9999)
    return code


def send_code_phone(phone: str):
    code = generate_code()
    cache.set(phone, code, timeout=REDIS_TIMEOUT)
    print(cache.get(phone))
    # TODO send code to  phone function
    # ...
