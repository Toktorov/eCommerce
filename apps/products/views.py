from django.shortcuts import render
from apps.products.models import Product
from apps.settings.models import Setting

# Create your views here.
def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    context = {
        'setting' : setting,
        'product' : product,
    }
    return render(request, 'item-detail-one.html', context)
    