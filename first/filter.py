from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from first.models import CarModel


def car_filter(query: QueryDict) -> QuerySet:
    queryset = CarModel.objects.all()

    for key, value in query.items():
        match key:
            case 'price_gt':
                queryset = queryset.filter(price__gt=value)
            case 'price_lt':
                queryset = queryset.filter(price__lt=value)
            case _:
                raise ValidationError(f"Filter {key} not supported")

    return queryset
