from django.db import models
from apps.users.models import User 
from apps.products.models import Product
import uuid

# Create your models here.
class Chat(models.Model):
    id_chat = models.CharField(
        max_length = 255, 
        default = uuid.uuid4,
        verbose_name = "Идентификатор чата"
    )
    from_chat_user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "from_user_chat",
        verbose_name = "От пользователя"
    )
    to_chat_user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        related_name = "to_user_chat",
        verbose_name = "К пользователю"
    )
    chat_product = models.ForeignKey(
        Product, 
        on_delete = models.CASCADE,
        related_name = "product_chat",
        verbose_name = "Продукт"
    )

    def __str__(self):
        return f"{self.id_chat}"

    class Meta:
        verbose_name = "Чат"
        verbose_name_plural = "Чаты"

class UserChat(models.Model):
    chat_id = models.ForeignKey(
        Chat, 
        on_delete = models.CASCADE,
        related_name = 'user_chat_id',
        verbose_name = "ID чата"
    )
    from_user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "chat_from_user",
        verbose_name = "Сообщение от пользователя"
    )
    to_user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = "chat_to_user",
        verbose_name = "Сообщение к пользователю"
    )
    message = models.CharField(
        max_length = 255,
        verbose_name = "Сообщение"
    )
    created = models.TimeField(
        auto_now_add = True
    )

    def __str__(self):
        return f"{self.chat_id} {self.message}"

    class Meta:
        verbose_name = "Сообщение в чате"
        verbose_name_plural = "Сообщение в чатах"