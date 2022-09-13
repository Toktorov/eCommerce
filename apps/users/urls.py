from django.urls import path 
from apps.users.views import register, user_login, profile, user_setting


urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', user_login, name = "user_login"),
    path('profile/<int:id>', profile, name = "profile"),
    path('setting/user/<int:id>', user_setting, name = "user_setting")
]   