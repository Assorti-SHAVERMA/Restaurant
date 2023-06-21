from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Menu, Category, Events, Testimonials, \
                    Gallery, Role, Chefs, Reservation, Contact


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name"]


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "description", "price", "created_at", "get_image"]
    list_editable = ["price"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ["full_name", "description", "profession", "created_at", "get_image"]
    list_filter = ["created_at", "profession"]
    search_fields = ["first_name", "last_name", "description"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price", "created_at", "get_image"]
    list_filter = ["created_at"]
    search_fields = ["title", "description"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title"]


@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ["full_name", "role", "twitter", "facebook", "instagram", "linkedin", "created_at", "get_image"]
    list_filter = ["role", "created_at"]
    list_editable = ["role"]
    search_fields = ["full_name"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "phone", "date", "time", "persons", "message", "created_at"]
    list_filter = ["date", "time",  "persons", "created_at"]
    search_fields = ["date", "time", "full_name"]


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ["get_image", "created_at"]
    list_filter = ["created_at"]

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100">')
        return "Not image"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "subject", "message", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["full_name", "email", "subject"]