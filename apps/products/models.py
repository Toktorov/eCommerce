from django.db import models
from apps.users.models import User
from apps.categories.models import Category

# Create your models here.
class Currency(models.Model):
    name_currency = models.CharField(
        max_length=50,
        verbose_name="Название валюты"
    )

    def __str__(self):
        return self.name_currency

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

class Product(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_product",
        verbose_name="Владелец товара"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название продукта"
    )
    description = models.CharField(
        max_length=300,
        verbose_name="Описание товара"
    )
    product_image = models.ImageField(
        upload_to = 'products_images/',
        verbose_name="Фотография продукта"
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена"
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name="product_currency",
        verbose_name="Название валюты",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="product_category",
        verbose_name="Категория товара"
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
