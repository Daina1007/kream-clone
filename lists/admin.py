from django.contrib import admin
from .models import list

# Register your models here.
@admin.register(list)
class listAdmin(admin.ModelAdmin):
    filter_horizontal = ("products",)
    list_display = ("__str__", "count_products")
