from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    customers = Customers.objects.all()
    order = Order.objects.all()
    total_cus = customers.count()
    tolal_ord = order.count()
    delivred = order.filter(cas='delivred').count()
    pending = order.filter(cas='pending').count()
    context = {'customers':customers , 'order':order ,'delivred':delivred ,'pending':pending , 'total_cus': total_cus ,'tolal_ord':tolal_ord}
    return render(request , 'account/dashboard.html',  context)

def products(request):
    products = Product.objects.all()
    return render(request,'account/products.html', {'products':products})

def customers(request):
    customers = Customers.objects.all()
    return render(request,'account/costumers.html', {'customers':customers})