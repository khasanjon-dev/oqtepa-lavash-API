from django.db.models import Model, ImageField, CharField, TextField, TimeField


class Settings(Model):
    # file
    logo = ImageField(upload_to='company/images')


class About(Model):
    title = CharField(max_length=250)
    text = TextField()
    # file
    image = ImageField(upload_to='company/images')


class Phone(Model):
    phone = CharField(max_length=9)


class Social(Model):
    name = CharField(max_length=250)
    link = CharField(max_length=250)


class Branch(Model):
    name = CharField(max_length=250)
    phone = CharField(max_length=9)
    open_week = CharField(max_length=50)
    close_week = CharField(max_length=50)

    # time
    open_time = TimeField()
    closing_time = TimeField()
