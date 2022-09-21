# Generated by Django 4.1.1 on 2022-09-21 09:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_moneytransfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneytransfer',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='money_transfer_user', to=settings.AUTH_USER_MODEL, verbose_name='Отправитель'),
            preserve_default=False,
        ),
    ]
