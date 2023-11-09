from django.db.models import CASCADE, ForeignKey, IntegerField, Model
from orders.models import Order
from products.models import Product


class OrderItem(Model):
    quantity = IntegerField()
    price = IntegerField()
    # relationships
    order = ForeignKey(Order, CASCADE)
    product = ForeignKey(Product, CASCADE)

    def __str__(self):
        return self.product.name + ' ' + self.order.address
