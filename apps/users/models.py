from django.db.models import Model, CharField, DateField, ForeignKey, CASCADE, TextField, DateTimeField

from products.models import Product


class User(Model):
    name = CharField(max_length=150)
    phone = CharField(max_length=9, unique=True)
    birth_date = DateField(null=True, blank=True)

    updated_at = DateTimeField(auto_now=True, null=True)
    created_at = DateTimeField(auto_now_add=True)


class Address(Model):
    customer = ForeignKey(User, CASCADE, 'address')
    full_address = TextField()
    description = TextField()


class Favorite(Model):
    customer = ForeignKey(User, CASCADE, 'favorites')
    product = ForeignKey(Product, CASCADE, 'favorites')

    def __str__(self):
        return self.product.name
