from django.contrib import admin
from apps.products.models import Product, Currency

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'price', 'currency', 'category', 'status_product', 'created')
    search_fields = ('user__username', 'title', 'price', 'currency__name_currency', 'category__title', 'status_product', 'created')

admin.site.register(Product, ProductAdmin)
admin.site.register(Currency)