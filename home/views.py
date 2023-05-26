from django.shortcuts import render
from django.views import View
from django.views import generic
from django.contrib import messages


class HomeView(View):

    def get(self, request, *args, **kwargs):
        template = 'home/index.html'
        return render(request, template)
