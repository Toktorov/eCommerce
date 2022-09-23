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

class Contact(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя")
    email = models.EmailField(
        verbose_name="Почта"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок"
    )
    message = models.CharField(
        max_length=255, 
        verbose_name="Сообщение"
    )
    status_contact = models.BooleanField(
        verbose_name="Статус обращения",
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
    
class AboutUs(models.Model):
    image = models.ImageField(
        upload_to = 'about_us/',
        verbose_name="Фотография"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Описание"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"