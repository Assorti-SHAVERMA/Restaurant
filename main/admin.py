from django.contrib import admin
from .models import Category, Product

from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["slug", "get_image", "name", "description", "price", "category"]
    list_filter = ["category", "created_at"]
    search_fields = ["name"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="150px">')
        return "not Image"

