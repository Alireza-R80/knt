from django.contrib import admin
from .models import *


@admin.register(Designer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('parent_user', 'card_number')


admin.site.register(Customer)
