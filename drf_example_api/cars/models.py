from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.fields import CharField, IntegerField, SmallIntegerField


class Car(models.Model):
    make = CharField(verbose_name="Manufacturer", max_length=50)
    model = CharField(verbose_name="Model name", max_length=50)
    model_year = IntegerField()
    rating = SmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    origin_country = CharField(max_length=50)
    category = CharField(max_length=40)
