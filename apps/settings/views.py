from django.shortcuts import render
from apps.settings.models import Setting
from apps.products.models import Product
from apps.users.models import User

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    products = Product.objects.all().order_by("?")
    users = User.objects.all().order_by("?")
    context = {
        'setting' : setting,
        'products' : products,
        'users' : users,
    }
    return render(request, 'index.html', context)