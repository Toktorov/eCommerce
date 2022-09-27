from django.contrib import admin
from apps.chats.models import Chat, UserChat

# Register your models here.
admin.site.register(Chat)
admin.site.register(UserChat)