from django.contrib import admin
from .models import *


class ProductImage(admin.TabularInline):
    model = ProductImage


class ProductTag(admin.TabularInline):
    model = ProductTag


class ProductDetail(admin.TabularInline):
    model = ProductDetail


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductDetail,
        ProductImage,
        ProductTag,
    ]

# Register your models here.
