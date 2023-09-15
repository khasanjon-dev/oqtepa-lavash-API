from django.db.models import Model, CharField, TextField, IntegerField


class Product(Model):
    name = CharField(max_length=150)
    composition = TextField()
    price = IntegerField()
    