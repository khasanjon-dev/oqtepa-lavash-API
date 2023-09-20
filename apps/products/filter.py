from django_filters import FilterSet, NumberFilter

from products.models import Product


class ProductFilterSet(FilterSet):
    category_id = NumberFilter('category_id', 'exact', required=True)

    class Meta:
        model = Product
        fields = {
            'category_id': ['exact'],
        }
