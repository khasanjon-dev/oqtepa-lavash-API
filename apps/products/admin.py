from django.contrib.admin import ModelAdmin, register
from django.utils.html import format_html
from products.models import Category, Product


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'description', 'price')


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'picture')

    @staticmethod
    def picture(obj):
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%"'.format(obj.icon.url))
