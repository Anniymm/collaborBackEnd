import django_filters
from .models import Product, Category

class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass

class ProductFilter(django_filters.FilterSet):
    categories = NumberInFilter(field_name='categories__id', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['categories']
