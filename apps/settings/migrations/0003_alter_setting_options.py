# Generated by Django 4.1.1 on 2022-09-07 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_alter_setting_linkedin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='setting',
            options={'verbose_name': 'Настройка', 'verbose_name_plural': 'Настройки'},
        ),
    ]
