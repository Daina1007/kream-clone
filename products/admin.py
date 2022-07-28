from django.contrib import admin
from .models import Brand, Photo, Product


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 1


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    inlines = [
        PhotoInline,
    ]

    list_display = ("brand", "name_en", "name_ko")

    search_fields = ("name_en", "name_ko", "brand__name")
    # brand__name이 의미하는 것이 brand의 name 필드값을 기준으로 검색한다는 뜻
    # brand와 product가 상관관계가 있으므로 가능한 일임


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
