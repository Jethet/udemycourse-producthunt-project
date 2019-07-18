from django.shortcuts import render

from .models import Product

def home(request):
    product = Product.objects
    return render(request, 'product/home.html', {'product':product})
