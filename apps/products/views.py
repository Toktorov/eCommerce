from django.shortcuts import render, redirect
from apps.products.models import Product, Currency
from apps.settings.models import Setting
from apps.categories.models import Category
from apps.users.models import User
from apps.chats.models import Chat 
from django.db.models import Q 

# Create your views here.
def product_detail(request, id):
    setting = Setting.objects.latest('id')
    product = Product.objects.get(id = id)
    random_product = Product.objects.all().order_by("?")[:4]
    if request.method == "POST":
        if 'chat' in request.POST:
            try:
                chat = Chat.objects.get(from_chat_user = request.user, chat_product = product)
                return redirect('chat_detail', chat.id_chat)
            except:
                chat = Chat.objects.create(from_chat_user = request.user, to_chat_user = product.user, chat_product = product)
                return redirect('chat_detail', chat.id_chat)
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
        if image and title and category and price and currency:
            product = Product.objects.create(user = request.user, title = title, description = description, product_image = image, category_id = category, price = price, currency_id = currency)
            return redirect('index')
        else:
            return redirect('product_create_error')
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
            if image:
                product = Product.objects.get(id = id)
                product.product_image = image 
                product.save()
                return redirect('product_detail', product.id)
            else:
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
            if user.status_user == False:
                user.balance -= 100
            else:
                user.balance -= 0
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

def product_search(request):
    products = Product.objects.all()
    setting = Setting.objects.latest('id')
    search_key = request.GET.get('key')
    if search_key:
        products = Product.objects.filter(Q(title__icontains = search_key))
    context = {
        'products' : products,
        'setting' : setting,
    }
    return render(request, 'settings/search_product.html', context)