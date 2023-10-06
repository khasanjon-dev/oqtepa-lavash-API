from django.db.models import ForeignKey, SET_NULL, Model, TextField, DateTimeField, BooleanField, TextChoices, CharField

from products.models import Product
from users.models import User


class Order(Model):
    class ReceptionType(TextChoices):
        DELIVERY = 'delivery', 'delivery'
        PICKUP = 'pickup', 'pickup'

    address = TextField()
    status = BooleanField(default=False)
    date = DateTimeField(auto_now_add=True)

    # choices
    reception_type = CharField(max_length=8, choices=ReceptionType.choices)

    # relationships
    product = ForeignKey(Product, SET_NULL, null=True)
    customer = ForeignKey(User, SET_NULL, null=True)

    def __str__(self):
        return self.customer.name + self.product.name
