from django.urls import path 
from apps.settings.views import (index, not_enough_money, 
no_settings, destination_not_found, contact, 
thank_you, about_us, news_detail, news_index, 
product_create_error, user_not_found,
register_error)

urlpatterns = [
    path('', index, name = "index"),
    path('news/', news_index, name = "news_index"),
    path('news/<int:id>', news_detail, name = "news_detail"),
    path('not_enough_money/', not_enough_money, name = "not_enough_money"),
    path('no_setting/', no_settings, name = "no_settings"),
    path('destination/not/found', destination_not_found, name = "destination_not_found"),
    path('contact/', contact, name = "contact"),
    path('thank_you/', thank_you, name = "thank_you"),
    path('about_us/', about_us, name = "about_us"),
    path('product/create/error/', product_create_error, name = "product_create_error"),
    path('user/not_found/', user_not_found, name = "user_not_found"),
    path('register/error/', register_error, name = "register_error")
]