from django.db.models import CharField, TextField, IntegerField, ForeignKey, CASCADE, Model


class Product(Model):
    name = CharField(max_length=150)
    description = TextField()
    price = IntegerField()

    # relationships
    category = ForeignKey('Category', CASCADE, 'products')

    def __str__(self):
        return self.name
