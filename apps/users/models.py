import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to = "profile_image/",
        verbose_name="Фотография профиля",
        blank = True, null = True,
        default = "profile_image/no_image.png"
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер",
        blank = True, null = True
    )
    balance = models.PositiveBigIntegerField(
        verbose_name="Баланс пользователя", 
        default = 0
    )
    wallet = models.CharField(
        default=uuid.uuid4,
        verbose_name="Кошелек",
        max_length=150,
        unique=True
    )
    status_user = models.BooleanField(
        verbose_name="Статус пользователя",
        default=False
    )

    def __str__(self):
        return self.username

class MoneyTransfer(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="money_transfer_user",
        verbose_name="Отправитель"
    )
    address_wallet = models.CharField(
        max_length=150,
        verbose_name="Адрес кошелька"
    )
    amount_money = models.PositiveIntegerField(
        verbose_name="Сумма кошелька"
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.address_wallet} {self.created}"