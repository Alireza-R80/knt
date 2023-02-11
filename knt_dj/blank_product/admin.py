from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

admin.site.register(Category, MPTTModelAdmin)


class BlankPropInline(admin.TabularInline):
    model = BlankProductProp


@admin.register(BlankProductType)
class BlankProductTypeAdmin(admin.ModelAdmin):
    inlines = [
        BlankPropInline
    ]


class BlankProductImageInline(admin.TabularInline):
    model = BlankProductImage


class BlankProductSampleImageInline(admin.TabularInline):
    model = BlankProductSampleImage


class BlankPropValueInline(admin.TabularInline):
    model = BlankProductPropValue


@admin.register(BlankProduct)
class BlankProductAdmin(admin.ModelAdmin):
    inlines = [
        BlankPropValueInline,
        BlankProductImageInline,
        BlankProductSampleImageInline,
    ]