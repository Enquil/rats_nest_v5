from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Category
from django.views import View


class ProductView(View):

    def get(self, request, *args, **kwargs):
        template = 'products/products.html'
        if 'q' in request.GET:
            query = request.GET['q']
        return render(request, template)
