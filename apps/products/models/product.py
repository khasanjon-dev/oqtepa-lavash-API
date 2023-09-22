from django.db.models import Model, ImageField, CharField, TextField, IntegerField, ForeignKey, CASCADE

from products.models import Category


class Product(Model):
    name = CharField(max_length=150)
    description = TextField()
    price = IntegerField()
    image = ImageField(upload_to='products/images')

    # relationships
    category = ForeignKey(Category, CASCADE, 'products')

    def __str__(self):
        return self.name
