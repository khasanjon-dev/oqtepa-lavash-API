from django.db.models import CharField, Model


class Category(Model):
    name = CharField(max_length=150)

    def __str__(self):
        return self.name
