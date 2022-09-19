from django.shortcuts import render
from apps.categories.models import Category
from apps.settings.models import Setting

# Create your views here.
def category_detail(request, slug):
    category = Category.objects.get(slug = slug)
    setting = Setting.objects.latest('id')
    categories = Category.objects.all().order_by("?")[:5]
    context = {
        'category' : category,
        'setting' : setting,
        'categories' : categories,
    }
    return render(request, 'categories/category_detail.html', context)