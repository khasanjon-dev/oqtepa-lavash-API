from django.db.models import CASCADE, ForeignKey, IntegerField, Model, BooleanField

from products.models import Product
from users.models import User


class Favorite(Model):
    # relationships
    customer = ForeignKey(User, CASCADE, 'favorites')
    product = ForeignKey(Product, CASCADE, 'favorites')
    is_like = BooleanField(default=True)

    class Meta:
        unique_together = ('customer', 'product')

    def __str__(self):
        return self.product.name


class Basket(Model):
    quantity = IntegerField(default=1)
    # relationships
    customer = ForeignKey(User, CASCADE, 'basket')
    product = ForeignKey(Product, CASCADE, 'basket')

    class Meta:
        unique_together = ('customer', 'product')

    def __str__(self):
        return self.customer.name + self.product.name
