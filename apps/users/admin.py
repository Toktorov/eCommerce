from django.contrib import admin
from apps.users.models import User, MoneyTransfer

# Register your models here.
admin.site.register(User)
admin.site.register(MoneyTransfer)