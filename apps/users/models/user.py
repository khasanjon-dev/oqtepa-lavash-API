from django.db.models import Model, CharField, DateField


class User(Model):
    name = CharField(max_length=150)
    phone = CharField(max_length=12)
    birth_date = DateField()
