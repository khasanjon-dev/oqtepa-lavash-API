from django.db.models import Model, ForeignKey, DateTimeField, CASCADE, IntegerField

from products.models import Product
from users.models import User, Address


class Order(Model):
    customer = ForeignKey(User, CASCADE)
    OrderAddress = ForeignKey(Address, CASCADE)

    date_order = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name


class OrderItem(Model):
    product = ForeignKey(Product, CASCADE)
    order = ForeignKey(Order, CASCADE)
    quantity = IntegerField(default=1)

    class Meta:
        unique_together = ('product', 'order')

    def __str__(self):
        return self.product.name + ' ' + str(self.quantity)
