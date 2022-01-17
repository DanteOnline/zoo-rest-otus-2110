from django_filters import rest_framework as filters
from .models import Kind


class KindFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Kind
        fields = ['name']
