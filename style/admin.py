from django.contrib import admin
from style.models import Style, Photo


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 5


# Register your models here.
@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline,
    ]

    filter_horizontal = ("product",)
    list_display = ("__str__", "count_style")
