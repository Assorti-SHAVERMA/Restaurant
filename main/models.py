from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
# Create your models here





class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

def slugify_fun(content):
    return slugify(content)

class Product(models.Model):

    # 3 variant это вариант читает str и делает каждый слаг уникальным и не дает возсожность редактировать
    slug = AutoSlugField(populate_from=slugify_fun, unique=True, editable=False)

    # Automatizing slug автоматический создает слаги по которому мы указали 2 Variant
    # slug = AutoSlugField(populate_from='name')

    #  created slug 1 Variant
    # slug = models.SlugField(max_length=100, unique=True, verbose_name="URL slug")

    image = models.ImageField(upload_to="product/", verbose_name="Image")
    name = models.CharField(max_length=100, verbose_name="Name product")
    description = models.TextField(verbose_name="Description")
    price = models.PositiveIntegerField(verbose_name="Price")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")


    def __str__(self) -> str:
        return f"{self.name} {self.price} {self.created_at}"
    

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        # показывает новые продукты
        ordering = ["-created_at"]

