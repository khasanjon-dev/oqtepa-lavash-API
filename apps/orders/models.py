from django.db.models import Model, ForeignKey, SET_NULL, DateTimeField, BooleanField, CASCADE, IntegerField


class Order(Model):
    customer = ForeignKey('User', SET_NULL, 'orders')
    OrderAddress = ForeignKey('Address', SET_NULL)

    date_order = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.name


class OrderItem(Model):
    product = ForeignKey('Product', SET_NULL)
    order = ForeignKey('Order', CASCADE)
    quantity = IntegerField(default=1)

    def __str__(self):
        return self.product.name + ' ' + str(self.quantity)
