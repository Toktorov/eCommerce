from django.contrib import admin
from apps.settings.models import Setting, Contact, AboutUs

# Register your models here.
admin.site.register(Setting)
admin.site.register(Contact)
admin.site.register(AboutUs)