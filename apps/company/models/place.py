from django.db.models import (CASCADE, CharField, FloatField, Model,
                              OneToOneField, TimeField)


class Branch(Model):
    name = CharField(max_length=200)
    phone = CharField(max_length=100)
    open_week = CharField(max_length=50)
    close_week = CharField(max_length=50)

    # time
    open_time = TimeField()
    closing_time = TimeField()

    def __str__(self):
        return self.name


class Location(Model):
    latitude = FloatField()
    longitude = FloatField()
    branch = OneToOneField(Branch, CASCADE)

    def __str__(self):
        return self.branch.name


class Region(Model):
    name = CharField(max_length=250)

    def __str__(self):
        return self.name
