from django.contrib import admin
from apps.users.models import User, MoneyTransfer

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # list_filter = ('username', )
    list_display = ('username', 'email', 'date_joined', 'balance', 'status_user')
    search_fields = ('wallet','username', 'email', 'date_joined', 'balance', 'status_user')

class MoneyTransferAdmin(admin.ModelAdmin):
    list_display = ('user', 'address_wallet', 'amount_money', 'created')
    search_fields = ('user__username', 'address_wallet', 'amount_money', 'created')

admin.site.register(User, UserAdmin)
admin.site.register(MoneyTransfer, MoneyTransferAdmin)