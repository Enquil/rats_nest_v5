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


class AddItem(View):
    '''
    View for adding an item to the shopping bag
    '''

    def post(self, request, item_id, *args, **kwargs):
        quantity = int(request.POST['quantity'])
        print(request.POST)
