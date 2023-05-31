from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Brand, Product
from django.views import View


class ProductView(View):

    def get(self, request, *args, **kwargs):

        products = Product.objects.all().order_by('-price')

        if 'domain' in request.GET:
            domain = request.GET['domain']
            products = Product.objects.filter(domain=domain)

        if 'q' in request.GET:
            q = request.GET['q']

        template = 'products/products.html'
        return render(request, template,
                      {"products": products})


class ProductDetail(View):
    """ Detailed view for chosen product """

    def get(self, request,  *args, **kwargs):

        return render(request, 'products/product_detail.html')
