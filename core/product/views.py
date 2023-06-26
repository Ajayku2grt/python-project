# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm
import pdb
from django.http import JsonResponse
from table import Table
from table.columns import Column

def product_list(request):    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data=[]
        products = Product.objects.all()  
        for product in products:
            data.append({
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'description': product.description,
                # Add other fields as needed
            })    
        return JsonResponse({'data': data})
    
    
    products = Product.objects.all()
    print('to procee',request)
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request, 'product_form.html', {'form': form})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})
