from django.shortcuts import render
from apps.settings.models import Setting
from apps.products.models import Product

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    products = Product.objects.all().order_by("?")
    context = {
        'setting' : setting,
        'products' : products,
    }
    return render(request, 'index.html', context)