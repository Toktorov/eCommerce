from django.urls import path 
from apps.users.views import register, user_login, profile, user_setting, pro_update_user, money_transfer, password_reset_send
from django.contrib.auth import views as auth_views #import this



urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', user_login, name = "user_login"),
    path('profile/<str:username>', profile, name = "profile"),
    path('setting/user/<int:id>', user_setting, name = "user_setting"),
    path('user/update/pro/<int:id>', pro_update_user, name = "pro_update_user"),
    path('user/money/transfer', money_transfer, name = "money_transfer"),
    path('password/reset/', password_reset_send, name = "password_reset_send"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),      
]   