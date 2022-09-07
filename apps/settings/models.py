from tabnanny import verbose
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название сайта"
    )
    description = models.TextField(
        verbose_name="Описание сайта"
    )
    logo = models.ImageField(
        upload_to = "logo/"
    )
    facebook = models.URLField(
        verbose_name="Ссылка на страницу facebook",
        blank = True, null = True
    )
    instagram = models.URLField(
        verbose_name="Ссылка на страницу instagram",
        blank = True, null = True
    )
    linkedin = models.URLField(
        verbose_name="Ссылка на страницу linkedin",
        blank = True, null = True
    )
    twitter = models.URLField(
        verbose_name="Ссылка на страницу twitter",
        blank = True, null = True
    )
    skype = models.URLField(
        verbose_name="Ссылка на skype",
        blank = True, null = True
    )
    telegram = models.URLField(
        verbose_name="Ссылка на telegram",
        blank = True, null = True
    )
    whatsapp = models.URLField(
        verbose_name="Ссылка на whatsapp",
        blank = True, null = True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"