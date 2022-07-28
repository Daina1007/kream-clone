from sqlite3 import Timestamp
from django.db import models
from core.models import TimeStampedModel


class list(TimeStampedModel):
    """관심상품 모델에 대한 정의"""

    products = models.ManyToManyField("products.Product", related_name="lists")
    users = models.OneToOneField(
        "users.User", related_name="list", on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.users}의 장바구니"

    def count_products(self):
        return self.products.count()

    count_products.short_descriptions = "상품 수"
