from django.db.models import ForeignKey, Model, TextField, DateTimeField, TextChoices, CharField, CASCADE, IntegerField

from users.models import User


class Order(Model):
    class ReceptionType(TextChoices):
        DELIVERY = 'delivery', 'Delivery'
        PICKUP = 'pickup', 'Pickup'

    class PaymentType(TextChoices):
        CASH = 'cash', 'Cash'
        CLICK = 'click', 'Click'

    address = TextField()
    delivery_price = IntegerField()
    total_price = IntegerField()
    created_date = DateTimeField(auto_now_add=True)
    # choices
    payment_method = CharField(max_length=5, choices=PaymentType.choices)
    reception_type = CharField(max_length=8, choices=ReceptionType.choices)
    # relationships
    customer = ForeignKey(User, CASCADE, 'orders')

    def __str__(self):
        return self.customer.name + ' ' + self.address
