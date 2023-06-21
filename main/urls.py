from django.urls import path, include

from .views import IndexView, ProductDetailView

urlpatterns = [
    path("", IndexView, name="index"),
    path('<slug:slug>/', ProductDetailView, name="product_detail")
]

