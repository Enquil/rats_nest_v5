from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from products.models import Category, Brand, Product, Domain
from django.views import View
from .forms import AddProductForm


class SiteManager(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'site_manager/site_manager.html', {
            'add_form': AddProductForm(),
        })
