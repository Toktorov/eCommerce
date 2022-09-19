# Generated by Django 4.1.1 on 2022-09-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_status', models.CharField(max_length=20, verbose_name='Статус продукта')),
            ],
            options={
                'verbose_name': 'Статус продукта',
                'verbose_name_plural': 'Статус продуктов',
            },
        ),
    ]