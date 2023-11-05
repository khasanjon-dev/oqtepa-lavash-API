from django.db.models import Model, FileField, ImageField, CharField, TextField


class Settings(Model):
    # file
    logo = FileField(upload_to='company/images')
    picture = ImageField(upload_to='company/images')
    qr_code = ImageField(upload_to='company/images')

    qr_text = CharField(max_length=250)
    phone = CharField(max_length=100)
    bot_url = CharField(max_length=250)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name_plural = 'Settings'


class About(Model):
    title = CharField(max_length=250)
    text = TextField()
    # file
    image = ImageField(upload_to='company/images')

    class Meta:
        verbose_name_plural = 'About'


class Phone(Model):
    phone_number = CharField(max_length=100)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name_plural = 'Phone'


class Social(Model):
    name = CharField(max_length=250)
    link = CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Social'
