from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OnlineOrder
from .models import Invoice

# Create your views here.

def index(request):
    if request.method == 'POST':
        order_form = OnlineOrder(request.POST)
        if order_form.is_valid():
            name = order_form.cleaned_data['name']
            surname = order_form.cleaned_data['surname']
            phone = order_form.cleaned_data['contact']    
            order_form.save();
            current_obj = Invoice.objects.get(name=name,surname=surname,contact=phone)
            messages.info(request, "Order has been recieved expect delivery within 12hours")
            return redirect('/order_invoice/'+str(current_obj.id))
        else:
            messages.info(request, "Enter valid data")
            return redirect('/')
    else:
        order_form = OnlineOrder()
        current_obj = {'id': 3}
    return render(request, 'index.html', {'order_form': order_form, 'current_obj': current_obj})

def order_invoice(request, pk):
    orders = Invoice.objects.get(id=pk)
    return render(request, "order_invoice.html", {'orders': orders})