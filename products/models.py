from django.db import models
from core.models import TimeStampedModel

# 실제로 표시되는 이름을 알려주는 메소드를 추가한 것
class Brand(TimeStampedModel):
    name = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.name


class Photo(TimeStampedModel):
    image = models.ImageField(upload_to="product/%Y/%m/%d/")
    product = models.ForeignKey("Product", on_delete=models.CASCADE)


class Product(TimeStampedModel):

    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    name_en = models.CharField(max_length=120)
    name_ko = models.CharField(max_length=120)
    model_number = models.CharField(max_length=80)
    released = models.DateField()
    color = models.CharField(max_length=120)
    released_price = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.brand}-{self.name_en}"

    class Meta:
        verbose_name_plural = "상품"
        # 복수형을 방지하기 위해서는 verbose_name_plural
        ordering = ["name_en", "name_ko"]

    # 변수랑 변수가 아닌 문자를 넣고 싶을 때
