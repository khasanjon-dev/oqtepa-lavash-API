from django.db.models import Model, ImageField, CharField, TextField, IntegerField, ForeignKey, CASCADE


class Category(Model):
    name = CharField(max_length=150)
    icon = ImageField(upload_to='products/category/icons')

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(max_length=150)
    description = TextField()
    price = IntegerField()

    # relationships
    category = ForeignKey('Category', CASCADE, 'products')

    def __str__(self):
        return self.name
