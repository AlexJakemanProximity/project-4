from django.shortcuts import render
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }
    
    return render(request, template, context)