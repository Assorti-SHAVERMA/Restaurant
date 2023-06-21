from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

class Menu(models.Model):
    image = models.ImageField(upload_to='food/', verbose_name='Изображение')
    title = models.CharField(max_length=150, verbose_name='Название блюд')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(max_length=500, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.title} - {self.category}"

    class Meta:
        verbose_name='Меню'
        verbose_name_plural='Меню'



class Events(models.Model):
    image = models.ImageField(upload_to='events/', verbose_name='Изображениие')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    price = models.PositiveIntegerField(verbose_name='Цена')
    description = models.TextField(max_length=500, verbose_name='Описание')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.title} - {self.price} - {self.created_at}"

    class Meta:
        verbose_name='Событие'
        verbose_name_plural='События'


class Reservation(models.Model):
    full_name = models.CharField(max_length=155, verbose_name='ФИО')
    email = models.EmailField(max_length=255, verbose_name='Почта')
    phone = models.CharField(max_length=12, verbose_name='Номер телефона')
    date = models.DateTimeField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    persons = models.PositiveIntegerField(verbose_name='Количество людей')
    message = models.TextField(max_length=500, verbose_name='Сообщение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self) -> str:
        return f"{self.full_name} - {self.phone} - {self.date} - {self.time} - {self.persons}"

    class Meta:
        verbose_name='Бронирование'
        verbose_name_plural='Бронирования'


class Testimonials(models.Model):
    image = models.ImageField(upload_to="testimonials/",
        verbose_name="Изображение", blank=True, null=True)
    first_name = models.CharField(verbose_name="Имя", max_length=120)
    last_name = models.CharField(verbose_name="Фамилия", max_length=120)
    description = models.TextField(verbose_name="Тематика", max_length=120)
    profession = models.CharField(verbose_name="Профессия", max_length=120)
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} | Профессия: {self.profession} | {self.created_at}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name='Изображение')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self) -> str:
        return f"Фотография была добавлена в {self.created_at}"

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Галерея"


class Role(models.Model):
    title = models.CharField(max_length=120, verbose_name='Роль')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')


    def __str__(self) -> str:
        return f"{self.title} - {self.created_at}"

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"


class Chefs(models.Model):
    image = models.ImageField(upload_to="testimonials/",
        verbose_name="Изображение", blank=True, null=True)
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, verbose_name="Роль павара")
    twitter  = models.URLField(blank=True, null=True, unique=True, verbose_name="twitter", max_length=300)
    facebook = models.URLField(blank=True, null=True, unique=True, verbose_name="facebook", max_length=300)
    instagram = models.URLField(blank=True, null=True, unique=True, verbose_name="instagram", max_length=300)
    linkedin = models.URLField(blank=True, null=True, unique=True, verbose_name="linkedin", max_length=300)
    created_at = models.DateTimeField(auto_now_add=True,
        verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.full_name} | {self.role} | {self.created_at}"

    class Meta:
        verbose_name = "Повар"
        verbose_name_plural = "Повары"


class Contact(models.Model):
    full_name = models.CharField(verbose_name="ФИО", max_length=120)
    email = models.EmailField(verbose_name="Email", max_length=120)
    subject = models.CharField(verbose_name="Тема", max_length=120)
    message = models.TextField(verbose_name="Сообщение", max_length=400)
    created_at = models.DateTimeField(auto_now_add=True,
            verbose_name="Дата создания")

    def __str__(self) -> str:
        return f"{self.full_name} | {self.subject} | {self.message} | {self.created_at}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class YourModel(models.Model):
    # Определение полей модели
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    field3 = models.DateTimeField(auto_now_add=True)