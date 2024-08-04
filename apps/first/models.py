from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.first.choices.body_type_choices import BodyTypeChoices


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=10, validators=(V.MinLengthValidator(2),))
    price = models.IntegerField(validators=(V.MinValueValidator(0), V.MaxValueValidator(99_999),))
    year = models.IntegerField(validators=(V.MinValueValidator(1990), V.MaxValueValidator(2090),))
    body_type = models.CharField(max_length=10, choices=BodyTypeChoices.choices)
