from django.db import models


class BodyTypeChoices(models.TextChoices):
    Sedan = 'Sedan',
    Coupe = 'Coupe',
    Hatch_back = 'Hatch_back',
    Hybrid = 'Hybrid'