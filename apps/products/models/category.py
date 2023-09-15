from django.db.models import Model, CharField


class Category(Model):
    name = CharField(max_length=150)
