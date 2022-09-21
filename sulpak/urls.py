"""sulpak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.settings.views import index, not_enough_money, no_settings, destination_not_found
from apps.products.views import product_detail
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    path('users/', include('apps.users.urls')),
    path('logout/', LogoutView.as_view(next_page = 'index'), name = "logout"),
    path('product/', include('apps.products.urls')),
    path('category/', include('apps.categories.urls')),
    path('not_enough_money/', not_enough_money, name = "not_enough_money"),
    path('no_setting/', no_settings, name = "no_settings"),
    path('destination/not/found', destination_not_found, name = "destination_not_found"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)