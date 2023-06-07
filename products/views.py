from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Brand, Product, Domain
from django.views import View


class ProductView(View):

    def get(self, request, *args, **kwargs):

        products = Product.objects.all()
        categories = Category.objects.all()
        children = None
        parent = None
        category_nav = None

        if 'domain' in request.GET:
            domain = get_object_or_404(Domain, pk=request.GET['domain'])
            categories_and_children = Category.objects.filter(domain=domain)

            categories = [item for item in categories_and_children
                          if item.parent is None]
            products = Product.objects.filter(
                        domain=domain).order_by('-price')

        if 'category' in request.GET:

            category = get_object_or_404(Category, pk=request.GET['category'])
            domain = get_object_or_404(Domain, name=category.domain)

            if category.is_parent:
                categories = Category.objects.filter(parent=category.pk)
                product_categories = [category.name for category in categories]
                products = Product.objects.filter(
                            category__name__in=product_categories)
            else:
                categories = Category.objects.filter(parent=category.parent.pk)
                products = Product.objects.filter(category=category)

        if 'q' in request.GET:
            q = request.GET['q']

        return render(request, 'products/products.html',
                      {
                        'domain': domain,
                        'products': products,
                        'categories': categories,
                        'children': children,
                        })


class ProductDetail(View):
    """ Detailed view for chosen product """

    def get(self, request, product_sku):

        product = get_object_or_404(Product, sku=product_sku)
        domain = str(product.category.domain)
        category_parent = str(product.category.parent)
        size_list = None

        if domain == 'clothing':
            if category_parent == 'shoes':
                size_list = ('35', '36', '37', '38', '39', '40',
                             '41', '42', '43', '44', '45', '46')
            else:
                size_list = ('XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL')

        return render(request, 'products/product_detail.html',
                      {
                        'product': product,
                        'category_parent': category_parent,
                        'size_list': size_list,
                      })
