from django.shortcuts import redirect, render
from cust_onboard.models import Order
from django.http import HttpResponse
from cust_onboard.forms import OrderForm

#create
def create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/onboarding')
            except:
                pass
    else:
        form = OrderForm()
    return render(request, 'index.html', {'form': form}) 

#read
def show(request):
    orders = Order.objects.all() # all the orders fetched
    return render(request, 'show.html', {'orders': orders}) # returns all orders

#update
def edit(request, id):
    order = Order.objects.get(cust_id= id)
    form = OrderForm(instance=order)
    return render(request, 'edit.html', {'order': order, 'form': form})

def update(request, id):
    order = Order.objects.get(cust_id= id)
    form = OrderForm(request.POST, instance= order)
    if form.is_valid():
        form.save()
        return redirect('/onboarding/') #redirects to the show
    return render(request, 'edit.html', {'order': order})

#delete 
def destroy(request, id):
    order = Order.objects.get(cust_id= id)
    order.delete()
    return redirect('/onboarding/')