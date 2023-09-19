from django.contrib.admin import register, ModelAdmin

from products.models import Product, Category


@register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'description', 'price')


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'icon')
