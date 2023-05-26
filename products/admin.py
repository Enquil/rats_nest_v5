from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'friendly_name',
        'name',
        'parent',
    )

    ordering = ('name', 'friendly_name', 'parent')