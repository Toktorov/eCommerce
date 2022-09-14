# Generated by Django 4.1.1 on 2022-09-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_phone_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image/', verbose_name='Фотография профиля'),
        ),
    ]