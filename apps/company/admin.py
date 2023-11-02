from django.contrib import admin

from company.models import Settings, About, Phone, Social, Branch, Location


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


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
