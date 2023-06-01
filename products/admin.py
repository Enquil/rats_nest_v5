from django.contrib import admin
from .models import Category, Brand, Product, Color
from django.shortcuts import get_object_or_404


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'friendly_name',
        'name',
        'parent',
    )

    ordering = ('pk',)


@admin.register(Brand)
class Brand(admin.ModelAdmin):

    list_display = (
        'pk',
        'friendly_name',
        'name',
    )

    ordering = ('friendly_name',)


@admin.register(Color)
class Color(admin.ModelAdmin):

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
        'category'
    )

    ordering = ('pk', 'name')

    actions = ['update_sku']

    def update_sku(self, request, queryset):

        for query in queryset:

            product = Product.objects.filter(pk=query.pk)

            if query.color is None:
                color = '000'
            else:
                color_mix = '000'.replace('0', '', len(str(query.color.pk)))
                color = color_mix + str(query.color.pk)

            sku_mix = [query.domain, query.category.pk,
                       query.brand.pk, query.pk, color]

            product.update(sku=''.join(map(str, sku_mix)))
