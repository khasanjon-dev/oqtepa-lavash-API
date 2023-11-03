from django.contrib import admin
from django.utils.html import format_html

from company.models import Settings, About, Phone, Social, Branch, Location


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'picture')

    @staticmethod
    def picture(obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%"'.format(obj.image.url))


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    pass


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass
