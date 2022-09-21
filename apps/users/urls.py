from django.urls import path 
from apps.users.views import register, user_login, profile, user_setting, pro_update_user, money_transfer


urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', user_login, name = "user_login"),
    path('profile/<str:username>', profile, name = "profile"),
    path('setting/user/<int:id>', user_setting, name = "user_setting"),
    path('user/update/pro/<int:id>', pro_update_user, name = "pro_update_user"),
    path('user/money/transfer', money_transfer, name = "money_transfer")
]   