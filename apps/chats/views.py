from django.shortcuts import render, redirect
from apps.settings.models import Setting
from apps.chats.models import Chat, UserChat
from apps.users.models import User 

# Create your views here.
def chat_index(request, id_user):
    setting = Setting.objects.latest('id')
    try:
        chats = Chat.objects.filter(from_chat_user = id_user)
        if len(chats) == 0:
            raise BaseException('Error')
    except:
        chats = Chat.objects.filter(to_chat_user = id_user)
    if request.method == "GET":
        user = User.objects.get(id = id_user)
        user.message_notification = False 
        user.save()
    context = {
        'setting' : setting,
        'chats' : chats,
    }
    return render(request, 'chats/chat_index.html', context)

def chat_detail(request, id_chat):
    setting = Setting.objects.latest('id')
    chat = Chat.objects.get(id_chat = id_chat)
    user_chat = UserChat.objects.filter(chat_id = chat.id)
    if request.method == "POST":
        message = request.POST.get('message')
        user_message = UserChat.objects.create(chat_id = chat, from_user = request.user, to_user = chat.to_chat_user, message = message)
        chat.to_chat_user.message_notification = True
        chat.to_chat_user.save()
        return redirect('chat_detail', chat.id_chat)
    context = {
        'setting' : setting, 
        'chat' : chat,
        'user_chat' : user_chat
    }
    return render(request, 'chats/chat_detail.html', context)