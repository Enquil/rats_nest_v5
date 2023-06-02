from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Brand, Product
from django.views import View


class ProductView(View):

    def get(self, request, *args, **kwargs):

        products = Product.objects.all().order_by('-price')
        categories = Category.objects.all()
        parent = None
        category_nav = None

        if 'category' in request.GET:
            category_pk = int(request.GET['category'])
            category = Category.objects.filter(pk=category_pk)
            if category_pk <= 3:
                categories = Category.objects.filter(parent=category_pk)
                products = Product.objects.filter(
                            domain=category_pk).order_by('-price')
                category_nav = [category]
            else:
                parent = Category.objects.filter(pk=category[0].parent.pk)
                categories = Category.objects.filter(parent=category[0].parent)
                category_nav = [parent, category]

        if 'q' in request.GET:
            q = request.GET['q']

        return render(request, 'products/products.html',
                      {
                        'products': products,
                        'categories': categories,
                        'category_nav': category_nav,
                        'parent': parent,
                        })


class ProductDetail(View):
    """ Detailed view for chosen product """

    def get(self, request, product_id):

        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'products/product_detail.html',
                      {
                        'product': product
                      })
