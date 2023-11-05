from django.db.models import ForeignKey, Model, TextField, DateTimeField, TextChoices, CharField, CASCADE, IntegerField

from users.models import User


class Order(Model):
    class ReceptionType(TextChoices):
        DELIVERY = 'delivery', 'Delivery'
        PICKUP = 'pickup', 'Pickup'

    address = TextField()
    created_date = DateTimeField(auto_now_add=True)
    delivery_price = IntegerField()
    # choices
    reception_type = CharField(max_length=8, choices=ReceptionType.choices)
    # relationships
    customer = ForeignKey(User, CASCADE, 'orders')

    def __str__(self):
        return self.customer.name + ' ' + self.address
