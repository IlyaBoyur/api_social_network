import django_filters as filters
from django_filters.rest_framework import FilterSet

from .models import Post


class PostFilter(FilterSet):
    author = filters.CharFilter(field_name='author__username')
    text = filters.CharFilter(field_name='text', lookup_expr='icontains')
    publicated = filters.DateFilter(field_name='pub_date',
                                    lookup_expr='contains')

    class Meta:
        model = Post
        fields = ('author', 'text', 'pub_date',)
