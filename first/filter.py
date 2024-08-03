from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from first.models import CarModel
from first.serializers import CarSerializer


def car_filter(query: QueryDict) -> QuerySet:
    queryset = CarModel.objects.all()

    for key, value in query.items():
        match key:
            case 'id_gt':
                queryset = queryset.filter(id__gt=value)
            case 'id_gte':
                queryset = queryset.filter(id__gte=value)
            case 'id_lt':
                queryset = queryset.filter(id__lt=value)
            case 'id_lte':
                queryset = queryset.filter(id__lte=value)

            case 'year_gt':
                queryset = queryset.filter(year__gt=value)
            case 'year_gte':
                queryset = queryset.filter(year__gte=value)
            case 'year_lt':
                queryset = queryset.filter(year__lt=value)
            case 'year_lte':
                queryset = queryset.filter(year__lte=value)

            case 'price_gt':
                queryset = queryset.filter(price__gt=value)
            case 'price_gte':
                queryset = queryset.filter(price__gte=value)
            case 'price_lt':
                queryset = queryset.filter(price__lt=value)
            case 'price_lte':
                queryset = queryset.filter(price__lte=value)

            case 'brand_startswith':
                queryset = queryset.filter(brand__startswith=value)
            case 'brand_endswith':
                queryset = queryset.filter(brand__endswith=value)
            case 'brand_contains':
                queryset = queryset.filter(brand__contains=value)

            case 'sort':
                fields = CarSerializer.Meta.fields
                fields = [*fields, *[f'-{field}' for field in fields]]

                if value not in fields:
                    raise ValidationError({'details': f'choose order from {", ".join(fields)}'})
                queryset = queryset.order_by(value)

            case _:
                raise ValidationError(f"Filter {key} not supported")

    return queryset
