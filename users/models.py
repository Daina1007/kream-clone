import black
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):

    SHOW_SIZE_CHOICES = [
        ("220", "220"),
        ("225", "225"),
        ("230", "230"),
        ("235", "235"),
        ("240", "240"),
        ("245", "245"),
        ("250", "250"),
        ("255", "255"),
        ("260", "260"),
        ("265", "265"),
        ("270", "270"),
        ("275", "275"),
        ("280", "280"),
        ("285", "285"),
        ("290", "290"),
        ("295", "295"),
        ("300", "300"),
    ]
    avatar = models.ImageField(blank=True, null=True, upload_to="style/%Y/%m/%d/")
    phone_number = models.CharField(max_length=11, unique=True)
    shoe_size = models.CharField(blank=True, choices=SHOW_SIZE_CHOICES, max_length=3)
    is_ad_message = models.BooleanField(default=False)
    is_ad_email = models.BooleanField(default=False)
