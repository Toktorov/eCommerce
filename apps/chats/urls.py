from django.urls import path 
from apps.chats.views import chat_detail, chat_index


urlpatterns = [
    path('user/<int:id_user>', chat_index, name = "chat_index"),
    path('<str:id_chat>/', chat_detail, name = "chat_detail")
]