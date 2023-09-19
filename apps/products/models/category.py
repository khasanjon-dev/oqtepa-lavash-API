from django.db.models import CharField, Model, ImageField


class Category(Model):
    name = CharField(max_length=150)
    icon = ImageField(upload_to='products/category/icons')

    def __str__(self):
        return self.name
