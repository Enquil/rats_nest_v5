from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Brand, Product, Domain
from django.views import View


class ProductView(View):

    def get(self, request, *args, **kwargs):

        categories = Category.objects.all()
        products = None
        parent = None
        category_nav = None

        if 'domain' in request.GET:
            domain = get_object_or_404(Domain, pk=request.GET['domain'])
            categories_and_children = Category.objects.filter(domain=domain)

            categories = [item for item in categories_and_children
                          if item.parent is None]
            products = Product.objects.filter(
                        domain=domain).order_by('-price')

        if 'q' in request.GET:
            q = request.GET['q']

        return render(request, 'products/products.html',
                      {
                        'domain': domain,
                        'products': products,
                        'categories': categories,
                        })


class ProductDetail(View):
    """ Detailed view for chosen product """

    def get(self, request, product_id):

        product = get_object_or_404(Product, pk=product_id)
        return render(request, 'products/product_detail.html',
                      {
                        'product': product
                      })
