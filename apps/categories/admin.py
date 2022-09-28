from django.contrib import admin
from apps.categories.models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title', )}
admin.site.register(Category, CategoryAdmin)