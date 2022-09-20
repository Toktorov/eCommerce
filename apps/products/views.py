from django.shortcuts import render, redirect
from apps.products.models import Product, Currency
from apps.settings.models import Setting
from apps.categories.models import Category
from apps.users.models import User

# Create your views here.
def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    random_product = Product.objects.all().order_by("?")[:4]
    context = {
        'setting' : setting,
        'product' : product,
        'random_product' : random_product
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

def update_product(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    categories = Category.objects.all()
    currencies = Currency.objects.all()
    if request.method == "POST":
        if 'update' in request.POST:
            title = request.POST.get('title')
            description = request.POST.get('description')
            category = request.POST.get('category')
            price = request.POST.get('price')
            currency = request.POST.get('currency')
            product = Product.objects.get(id = id)
            product.title = title 
            product.description = description
            product.category_id = category
            product.price = price 
            product.currency_id = currency
            product.save()
            return redirect('product_detail', product.id)
        if 'delete' in request.POST:
            product = Product.objects.get(id = id)
            product.delete()
            return redirect('index')
        if 'product_image' in request.POST:
            image = request.FILES.get('image')
            product = Product.objects.get(id = id)
            product.product_image = image 
            product.save()
            return redirect('product_detail', product.id)
    context = {
        'setting' : setting,
        'product' : product,
        'categories' : categories,
        'currencies' : currencies
    }
    return render(request, 'products/update.html', context)

def pro_product_update(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    if request.method == "POST":
        try:
            user = User.objects.get(id = request.user.id)
            user.balance -= 100
            product.status_product = True 
            user.save()
            product.save()
            return redirect('product_detail', product.id)
        except:
            return redirect('not_enough_money')
    context = {
        'setting' : setting,
        'product' : product,
    }
    return render(request, 'products/pro_product.html', context)