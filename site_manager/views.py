from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Category, Brand, Product, Domain
from django.views import View
from .forms import AddProductForm
from django.http import (HttpResponse,
                         HttpResponseRedirect)


class SiteManager(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'site_manager/site_manager.html', {
            'add_product_form': AddProductForm(),
            })

    def post(self, request, *args, **kwargs):

        add_product_form = AddProductForm(request.POST, request.FILES)

        if add_product_form.is_valid():
            form = add_product_form.save(commit=False)
            form.save()
            return render(request, ('site_manager/site_manager.html'))
        else:
            add_product_form = AddProductForm()
