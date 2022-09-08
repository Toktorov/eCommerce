from tabnanny import verbose
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название категории"
    )
    slug = models.SlugField(
        verbose_name="Человекопонятный URL"
    )

    def __str__(self):
        return f"{self.title} {self.slug}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"