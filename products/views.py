from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Brand, Product
from django.views import View


class ProductView(View):

    def get(self, request, *args, **kwargs):

        products = Product.objects.all().order_by('-price')

        if 'category' in request.GET:
            category = int(request.GET['category'])
            if category <= 3:
                products = Product.objects.filter(
                            domain=category).order_by('-price')
            else:
                products = Product.objects.filter(
                            category=category).order_by('-price')

        if 'q' in request.GET:
            q = request.GET['q']

        return render(request, 'products/products.html',
                      {
                        'products': products
                        })


class ProductDetail(View):
    """ Detailed view for chosen product """

    def get(self, request, product_id):

        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'products/product_detail.html',
                      {
                        'product': product
                      })
