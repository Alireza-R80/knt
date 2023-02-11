from django.contrib import admin

# Register your models here.
from account.models import BaseUser, Designer


@admin.register(Designer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('parent_user', 'card_number')


admin.site.register(BaseUser)
