from django.db.models import Model, ForeignKey, CASCADE, TextField, IntegerField

from products.models import Product
from users.models import User


class Address(Model):
    customer = ForeignKey(User, CASCADE, 'address')
    full_address = TextField()
    description = TextField()

    def __str__(self):
        return self.full_address


class Favorite(Model):
    customer = ForeignKey(User, CASCADE, 'favorites')
    product = ForeignKey(Product, CASCADE, 'favorites')

    class Meta:
        unique_together = ('customer', 'product')

    def __str__(self):
        return self.product.name


class Basket(Model):
    customer = ForeignKey(User, CASCADE, 'basket')
    product = ForeignKey(Product, CASCADE, 'basket')
    quantity = IntegerField(default=1)

    class Meta:
        unique_together = ('customer', 'quantity')

    def __str__(self):
        return self.customer.name + self.product.name
