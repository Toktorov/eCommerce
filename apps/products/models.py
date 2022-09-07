from tabnanny import verbose
from django.db import models

# Create your models here.
class Product(models.Model):
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

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
