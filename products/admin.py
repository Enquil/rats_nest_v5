from django.contrib import admin
from .models import Category, Brand


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
