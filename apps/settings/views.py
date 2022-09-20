from django.shortcuts import render
from apps.settings.models import Setting
from apps.products.models import Product
from apps.users.models import User
from apps.categories.models import Category

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    products = Product.objects.all().order_by("?")[:20]
    random_product = Product.objects.all().order_by("?").filter(status_product = True)[:1]
    users = User.objects.all().order_by("?")
    categories = Category.objects.all().order_by("?")[:5]
    context = {
        'setting' : setting,
        'products' : products,
        'users' : users,
        'random_product' : random_product,
        'categories' : categories,
    }
    return render(request, 'index.html', context)

def not_enough_money(request):
    return render(request, 'not_enough_money.html')