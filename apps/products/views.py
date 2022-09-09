from django.shortcuts import render, redirect
from apps.products.models import Product, Currency
from apps.settings.models import Setting
from apps.categories.models import Category

# Create your views here.
def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    context = {
        'setting' : setting,
        'product' : product,
    }
    return render(request, 'products/item-detail-one.html', context)

def create_product(request):
    setting = Setting.objects.latest('id')
    categories = Category.objects.all()
    currency = Currency.objects.all()
    if request.method == "POST":
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        currency = request.POST.get('currency')
        product = Product.objects.create(user = request.user, title = title, description = description, product_image = image, category_id = category, price = price, currency_id = currency)
        return redirect('index')
    context = {
        'setting' : setting,
        'categories' : categories,
        'currency' : currency,
    }
    return render(request, 'products/upload_product.html', context)
    