from django.db import models
from core.models import TimeStampedModel
from users.models import User


class Photo(TimeStampedModel):
    image = models.ImageField(upload_to="style/%Y/%m/%d/")
    style = models.ForeignKey("Style", on_delete=models.CASCADE)


class Style(TimeStampedModel):
    comment = models.CharField(max_length=300, verbose_name="내용")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField("products.Product", related_name="style_list")

    def __str__(self) -> str:
        return f"{self.user}의 STYLE"

    def count_style(self):
        return self.product.count()

    count_style.short_description = "상품 태그 수"
    # count_products.short_descriptions = "상품 수"
