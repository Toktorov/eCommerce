from django.urls import path 
from apps.users.views import register, user_login, profile


urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', user_login, name = "user_login"),
    path('profile/<int:id>', profile, name = "profile")
]   