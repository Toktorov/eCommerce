from django.shortcuts import render, redirect
from apps.users.models import User
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

def profile(request, id):
    user = User.objects.get(id = id)
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
            return redirect('profile', user.id)
        if 'update_profile_image' in request.POST:
            profile_image = request.FILES.get('profile_image')
            user = User.objects.get(id = id)
            user.profile_image = profile_image
            user.save()
            return redirect('profile', user.id)
        if 'delete' in request.POST:
            user = User.objects.get(id = id)
            user.delete()
            return redirect('index')
    context = {
        'user' : user,
        'setting' : setting,
    }
    return render(request, 'users/creator-profile-edit.html', context)