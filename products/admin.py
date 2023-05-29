from django.contrib import admin
from .models import Category, Brand, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'friendly_name',
        'name',
        'parent',
    )

    ordering = ('name', 'friendly_name', 'parent')


@admin.register(Brand)
class Brand(admin.ModelAdmin):

    list_display = (
        'pk',
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'name',
        'sku',
    )

    ordering = ('name', 'pk')
