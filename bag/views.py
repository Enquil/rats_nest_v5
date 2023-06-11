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
        size = None

        if 'size' in request.POST:
            size = request.POST['size']

        bag = request.session.get('bag', {})
        if size:
            if item_id in list(bag.keys()):
                if size in bag[item_id]['items_by_size'].keys():
                    bag[item_id]['items_by_size'][size] += quantity
                else:
                    bag[item_id]['items_by_size'][size] = quantity
            else:
                bag[item_id] = {'items_by_size': {size: quantity}}
        else:
            if item_id in list(bag.keys()):
                bag[item_id] += quantity
            else:
                bag[item_id] = quantity
        print(bag)
        request.session['bag'] = bag
        return HttpResponseRedirect(reverse('product_detail', args=[sku]))
