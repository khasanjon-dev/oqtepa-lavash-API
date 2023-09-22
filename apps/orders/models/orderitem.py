from django.db.models import Model, ForeignKey, PositiveIntegerField, CASCADE

from orders.models import Order
from products.models import Product


class OrderItem(Model):
    quantity = PositiveIntegerField()

    # relationships
    order = ForeignKey(Order, CASCADE)
    product = ForeignKey(Product, CASCADE)

    def __str__(self):
        return self.product.name + ' ' + str(self.quantity)
