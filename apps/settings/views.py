from django.shortcuts import render, redirect
from django.core.mail import send_mail
from apps.settings.models import AboutUs, Setting, Contact, News
from apps.products.models import Product
from apps.users.models import User
from apps.categories.models import Category

# Create your views here.
def index(request):
    try:
        setting = Setting.objects.latest('id')
    except:
        return redirect('no_settings')
    products = Product.objects.all().order_by("?")[:20]
    random_product = Product.objects.all().order_by("?").filter(status_product = True, activity_product = True)[:1]
    users = User.objects.all().order_by("?")
    categories = Category.objects.all().order_by("?")[:5]
    news = News.objects.all()
    context = {
        'setting' : setting,
        'products' : products,
        'users' : users,
        'random_product' : random_product,
        'categories' : categories,
        'news' : news,
    }
    return render(request, 'index.html', context)

def not_enough_money(request):
    return render(request, 'settings/not_enough_money.html')

def no_settings(request):
    return render(request, 'settings/no_settings.html')

def destination_not_found(request):
    return render(request, 'users/destination_not_found.html')

def thank_you(request):
   return render(request, 'settings/thank_you.html')

def product_create_error(request):
    return render(request, 'settings/product_create_error.html')

def user_not_found(request):
    return render(request, 'settings/user_not_found.html')

def register_error(request):
    return render(request, 'settings/register_error.html')

def current_password_error(request):
    return render(request, 'settings/current_password_error.html')

def passwords_are_different(request):
    return render(request, 'settings/passwords_are_different.html')

def about_us(request):
    setting = Setting.objects.latest('id')
    about = AboutUs.objects.latest('id')
    users = User.objects.all()
    product = Product.objects.all()
    category = Category.objects.all()
    context = {
        'setting' : setting,
        'about' : about,
        'users' : users,
        'product' : product,
        'category' : category,
    }
    return render(request, 'settings/aboutus.html', context)

def contact(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')
        contact = Contact.objects.create(name = name, email = email, title = title, message = message)
        send_mail(
                    # title:
                    f"{setting.title}",
                    # message:
                    f"{name} спасибо за ваше сообщение. В скором времени мы вам ответим. Ваше сообщение {message}",
                    # from:
                    "noreply@somehost.local",
                    # to:
                    [email]
            )
        return redirect('thank_you')
    context = {
        'setting' : setting,
    }
    return render(request, 'settings/contact.html', context)

def news_detail(request, id):
    setting = Setting.objects.latest('id')
    news = News.objects.get(id = id)
    context = {
        'setting' : setting,
        'news' : news,
    }
    return render(request, 'settings/news_detail.html', context)

def news_index(request):
    setting = Setting.objects.latest('id')
    news = News.objects.all()
    context = {
        'setting' : setting,
        'news' : news
    }
    return render(request, 'settings/news_index.html', context)