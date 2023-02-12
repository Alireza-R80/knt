from django.contrib import admin
from .models import Size, Color, City, State

admin.site.register(Size)
admin.site.register(Color)
admin.site.register(State)
admin.site.register(City)

# Register your models here.
