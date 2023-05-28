from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category, Brand
from django.views import View


class ProductView(View):

    def get(self, request, query, *args, **kwargs):
        if query == 'search-query':
            meow = request.GET['q']
            print(meow)
        template = 'products/products.html'
        return render(request, template)
