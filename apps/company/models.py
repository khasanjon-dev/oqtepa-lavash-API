from django.db.models import Model, ImageField, CharField, TextField, TimeField, FloatField, OneToOneField, CASCADE, \
    JSONField


class Settings(Model):
    # file
    logo = ImageField(upload_to='company/images')
    picture = ImageField(upload_to='company/images')
    qr_code = ImageField(upload_to='company/images')
    qr_text = CharField(max_length=250, default='hello')
    contacts = JSONField(default=dict)

    class Meta:
        verbose_name_plural = 'Settings'


class About(Model):
    title = CharField(max_length=250)
    text = TextField()
    # file
    image = ImageField(upload_to='company/images')


class Phone(Model):
    phone_number = CharField(max_length=100)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name_plural = 'Phone'


class Social(Model):
    name = CharField(max_length=250)
    link = CharField(max_length=250)


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
