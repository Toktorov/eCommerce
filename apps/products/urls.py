from django.urls import path 
from apps.products.views import product_detail, create_product, update_product, pro_product_update, product_search


urlpatterns = [
    path('<int:id>', product_detail, name = "product_detail"),
    path('create/', create_product, name = "create_product"),
    path('update/<int:id>', update_product, name = "update_product"),
    path('update_pro/product/<int:id>', pro_product_update, name = "pro_product_update"),
    path('search/', product_search, name = "product_search")
]