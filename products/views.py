from django.shortcuts import render
from django.views import View
from django.views import generic
from django.contrib import messages


class ProductView(View):

    def get(self, request, *args, **kwargs):
        template = 'products/products.html'
        return render(request, template)
