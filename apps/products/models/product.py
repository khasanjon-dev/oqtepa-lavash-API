from django.db.models import (CASCADE, CharField, ForeignKey, ImageField,
                              IntegerField, Model, TextField)
from products.models import Category


class Product(Model):
    name = CharField(max_length=150)
    description = TextField()
    price = IntegerField()
    # file
    image = ImageField(upload_to='products/images')
    # relationships
    category = ForeignKey(Category, CASCADE, 'products')

    def __str__(self):
        return self.name
