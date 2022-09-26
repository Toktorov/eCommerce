from django.urls import path 
from apps.settings.views import index, not_enough_money, no_settings, destination_not_found, contact, thank_you, about_us, news_detail, news_index

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
]