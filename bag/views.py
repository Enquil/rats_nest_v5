from django.shortcuts import render
from django.views import View
from django.contrib import messages


class BagView(View):
    '''
    Bag View
    '''
    def get(self, request, *args, **kwargs):
        template = 'bag/bag.html'
        return render(request, template)
