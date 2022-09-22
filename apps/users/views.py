from django.shortcuts import render, redirect
from apps.users.models import User, MoneyTransfer
from apps.settings.models import Setting
from django.contrib.auth import login, authenticate

# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create(username = username, email = email)
            user.set_password(password)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        else:
            return redirect('register')
    context = {
        'setting' : setting,
    }
    return render(request, 'users/signup.html', context)

def user_login(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username = username)
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('index')
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