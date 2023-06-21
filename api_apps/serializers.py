from rest_framework import serializers
from food.models import Category, Menu, Events, Reservation, \
                    Testimonials, Gallery, Role, Chefs, Contact

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'image', 'title', 'category', 'description', 'price', 'created_at']


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'image', 'title', 'price', 'description', 'created_at']


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'full_name', 'email', 'phone', 'date', 'time', 'persons', 'message', 'created_at']


class TestimonialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonials
        fields = ['id', 'image', 'first_name', 'last_name', 'description', 'profession', 'created_at']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image', 'created_at']

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'title', 'created_at']


class ChefsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chefs
        fields = ['id', 'image', 'full_name', 'role', 'twitter', 'facebook', 'instagram', 'linkedin', 'created_at']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'email', 'subject', 'message', 'created_at']