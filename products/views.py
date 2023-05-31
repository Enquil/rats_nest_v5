from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Brand, Product
from django.views import View


class ProductView(View):

    def get(self, request, query, *args, **kwargs):
        products = Product.objects.all().order_by('-price')
        if query == 'search-query':
            meow = request.GET['q']
            print(meow)
        template = 'products/products.html'
        return render(request, template,
                      {"products": products})


class ProductView(View):

    def get(self, request, query, *args, **kwargs):

        products = Product.objects.all().order_by('-price')

        if query == 'search-query':
            q = request.GET['q']

        template = 'products/products.html'
        return render(request, template,
                      {"products": products})


# class ProductDetail(View):
#     """ Detailed view for chosen product """

#     def get(self, request,  *args, *kwargs)


#     return render(request, 'products/product_detail.html', context)
