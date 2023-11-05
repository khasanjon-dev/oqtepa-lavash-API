from django.db.models import Model, ForeignKey, CASCADE, IntegerField

from orders.models import Order
from products.models import Product


class OrderItem(Model):
    quantity = IntegerField()
    unit_price = IntegerField()
    # relationships
    order = ForeignKey(Order, CASCADE)
    product = ForeignKey(Product, CASCADE)

    def total_price(self):
        return self.unit_price * self.quantity

    def __str__(self):
        return self.product.name + ' ' + self.order.address
