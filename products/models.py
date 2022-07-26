from tkinter import CASCADE
from django.db import models
from core.models import TimeStampedModel


class Brand(TimeStampedModel):
    name = models.CharField(max_length=40)


class Photo(TimeStampedModel):
    image = models.ImageField()
    product = models.ForeignKey("Product", on_delete=CASCADE)


class Product(TimeStampedModel):

    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    name_en = models.CharField(max_length=120)
    name_ko = models.CharField(max_length=120)
    model_number = models.CharField(max_length=80)
    released = models.DateField()
    color = models.CharField(max_length=120)
    released_price = models.PositiveIntegerField()
