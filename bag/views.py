from products.models import Product
from django.views import View
from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.http import (HttpResponse,
                         HttpResponseRedirect)
from django.contrib import messages


class BagView(View):
    '''
    Bag View
    '''
    bag = request.session.get('bag', {})

    def get(self, request, *args, **kwargs):
        template = 'bag/bag.html'
        return render(request, template)


class AddItem(View):
    '''
    View for adding an item to the shopping bag
    '''

    def post(self, request, item_id, *args, **kwargs):

        product = get_object_or_404(Product, pk=item_id)
        quantity = int(request.POST['quantity'])
        sku = int(request.POST['sku'])

        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

        request.session['bag'] = bag
        return HttpResponseRedirect(reverse('product_detail', args=[sku]))
