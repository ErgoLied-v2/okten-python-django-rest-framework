from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet):
    year_gt = filters.NumberFilter('year', 'gt')
    year_lt = filters.NumberFilter('year', 'lt')