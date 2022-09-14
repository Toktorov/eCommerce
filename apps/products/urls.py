from django.urls import path 
from apps.products.views import product_detail, create_product, update_product


urlpatterns = [
    path('<int:id>', product_detail, name = "product_detail"),
    path('create/', create_product, name = "create_product"),
    path('update/<int:id>', update_product, name = "update_product")
]