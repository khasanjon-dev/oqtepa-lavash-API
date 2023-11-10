from django.db.models import (CASCADE, CharField, DateTimeField, ForeignKey,
                              IntegerField, Model, TextChoices, TextField)

from users.models import User


class Order(Model):
    class ReceptionType(TextChoices):
        DELIVERY = 'delivery', 'Delivery'
        PICKUP = 'pickup', 'Pickup'

    class PaymentType(TextChoices):
        CASH = 'cash', 'Cash'
        CLICK = 'click', 'Click'

    class Status(TextChoices):
        PENDING = 'pending', 'Pending'
        COMPLETED = 'completed', 'Completed'
        CANCEL = 'cancel', 'Cancel'
        SHIPPED = 'shipped', 'Shipped'

    address = TextField()
    delivery_price = IntegerField()
    total_price = IntegerField()
    created_date = DateTimeField(auto_now_add=True)
    # choices
    status = CharField(max_length=20, choices=Status.choices)
    payment_method = CharField(max_length=5, choices=PaymentType.choices)
    reception_type = CharField(max_length=8, choices=ReceptionType.choices)
    # relationships
    customer = ForeignKey(User, CASCADE, 'orders')

    def __str__(self):
        return self.customer.name + ' ' + self.address

