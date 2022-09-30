from django.shortcuts import render, redirect
from apps.settings.views import news_detail
from apps.users.models import User, MoneyTransfer
from apps.settings.models import Setting
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if username and email and password and confirm_password:
                try:
                    user = User.objects.create(username = username, email = email)
                    user.set_password(password)
                    user.save()
                    user = User.objects.get(username = username)
                    user = authenticate(username = username, password = password)
                    login(request, user)
                    return redirect('index')
                except:
                    return redirect('register_error')
            else:
                return redirect('register_error')
        else:
            return redirect('register_error')
    context = {
        'setting' : setting,
    }
    return render(request, 'users/signup.html', context)

def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return redirect('user_not_found')
    context = {
        'setting' : setting,
    }
    return render(request, 'users/login.html', context)

def profile(request, username):
    user = User.objects.get(username = username)
    setting = Setting.objects.latest('id')
    context = {
        'user' : user,
        'setting' : setting
    }
    return render(request, 'users/creator-profile.html', context)

def user_setting(request, id):
    user = User.objects.get(id = id)
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        if 'update' in request.POST:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            user = User.objects.get(id = id)
            user.username = username 
            user.first_name = first_name
            user.last_name = last_name
            user.email = email 
            user.phone = phone 
            user.save()
            return redirect('profile', user.username)
        if 'update_profile_image' in request.POST:
            profile_image = request.FILES.get('profile_image')
            user = User.objects.get(id = id)
            user.profile_image = profile_image
            user.save()
            return redirect('profile', user.username)
        if 'delete' in request.POST:
            user = User.objects.get(id = id)
            user.delete()
            return redirect('index')
        if 'update_password' in request.POST:
            password = request.POST.get('password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                try:
                    user = User.objects.get(username = request.user)
                    if user.check_password(password):
                        user.set_password(new_password)
                        user.save()
                        return redirect('profile', user.username)
                    else:
                        return redirect('current_password_error')
                except:
                    return redirect('user_not_found')
            else:
                return redirect('passwords_are_different')
           
    context = {
        'user' : user,
        'setting' : setting,
    }
    return render(request, 'users/creator-profile-edit.html', context)

def pro_update_user(request, id):
    setting = Setting.objects.latest('id')
    user = User.objects.get(id = id)
    if request.method == "POST":
        try:
            user = User.objects.get(id = id)
            user.balance -= 1000
            user.status_user = True 
            user.save()
            return redirect('profile', user.username)
        except:
            return redirect('not_enough_money')
    context = {
        'setting' : setting,
        'user' : user,
    }
    return render(request, 'users/user_update_pro.html', context)

def money_transfer(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        address_wallet = request.POST.get('address_wallet')
        amount = request.POST.get('amount')
        sender = User.objects.get(username = request.user)
        try:
            try:
                destination = User.objects.get(wallet = address_wallet)
            except:
                return redirect('destination_not_found')
            sender.balance -= int(amount)
            sender.save()
        except:
            return redirect('not_enough_money')
        try:
            destination.balance += int(amount)
            destination.save()
        except:
            return redirect('destination_not_found')
        transfer_money = MoneyTransfer.objects.create(user = request.user, address_wallet = address_wallet, amount_money = amount)
        return redirect('index')
    context = {
        'setting' : setting,
    }
    return render(request, 'users/money_transfer.html', context)

def password_reset_send(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            check_email = User.objects.get(email = email)
            print(check_email)
            send_mail(
                    # title:
                    f"Восстановить пароль",
                    # message:
                    f"Привет {check_email.username}! Мы получили запрос на сброс пароля для учетной записи Sulpak, связанной с {email}. Перейдите по ссылке чтобы восстановить доступ к аккаунту http:// 192.168.0.139:8000/users/reset/{urlsafe_base64_encode(force_bytes(check_email.pk))}/{default_token_generator.make_token(check_email)}",
                    # from:
                    "noreply@somehost.local",
                    # to:
                    [email]
            )
            return HttpResponse("Сообщение со сброс успешно отправлена!")
        except:
            return HttpResponse("Почта не найдена")
    return render(request, 'users/password_reset.html')