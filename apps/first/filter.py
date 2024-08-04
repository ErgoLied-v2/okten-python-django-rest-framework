from django_filters import rest_framework as filters

from apps.first.choices.body_type_choices import BodyTypeChoices


class CarFilter(filters.FilterSet):
    year_gt = filters.NumberFilter('year', 'gt')
    year_lt = filters.NumberFilter('year', 'lt')
    year_range = filters.RangeFilter('year')
    year_in = filters.BaseInFilter('year')
    body = filters.ChoiceFilter('body_type', choices=BodyTypeChoices.choices)
    order = filters.OrderingFilter(fields=(
        ('id', 'car_id'),
        'brand',
        'price'
    ))
