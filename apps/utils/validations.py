import re


def is_phone_number(phone: str):
    pattern = r'^(?:\+998|998|)([1-9]\d{8})$'
    match = re.match(pattern, phone)
    if match:
        return True
    else:
        return False
