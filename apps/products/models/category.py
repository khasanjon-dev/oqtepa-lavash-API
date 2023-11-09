from django.db.models import CharField, ImageField, Model


class Category(Model):
    name = CharField(max_length=150)
    # file
    icon = ImageField(upload_to='products/category/icons')

    def __str__(self):
        return self.name

