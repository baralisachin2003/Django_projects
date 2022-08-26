from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages
import os
from django.contrib.auth.decorators import login_required
from accounts.auth import admin_only
from user_page.models import Order

# Create your views here.

#function to show categoryform
@login_required
@admin_only
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'category added successfully')
            return redirect('/admin/addcategory')
        else:
            messages.add_message(request,messages.ERROR,'please verify the form field')
            return render(request,'demo/addcategory.html',{
                'form':CategoryForm
            })
    context ={
        'form' : CategoryForm
    }
    return render(request,'demo/addcategory.html',context)

# function to show productform 
@login_required
@admin_only
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Product added successfully')
            return redirect('/admin/addproduct')
        else:
            messages.add_message(request,messages.ERROR,'please verify form fields')
            return render(request,'demo/addproduct.html',{
                'form':form
            })
    context = {
        'form' : ProductForm
    }
    return render(request,'demo/addproduct.html',context)

# function to show product 
@login_required
@admin_only
def show_product(request):
    product = Product.objects.all()
    context = {
        'product': product
    }
    return render(request,'demo/showproduct.html',context)

#function to show category 
@login_required
@admin_only
def show_category(request):
    category = Category.objects.all()
    
    context = {
        'category': category
    }
    return render(request,'demo/showcategory.html',context)


#function to delete the category
@login_required
@admin_only
def category_delete(request,category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    messages.add_message(request,messages.SUCCESS,'Category deleted successfully')
    return redirect('/admin/category')

#function to update category 
@login_required
@admin_only
def category_update(request,category_id):
    category = Category.objects.get(id = category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Category updated successfully')
            return redirect('/admin/category')
        else:
            messages.add_message(request,messages.ERROR,'Unable to update category')
            return render(request,'demo/updatecategory.html',{
                'form': form
            })
    context = {
        'form': CategoryForm(instance=category)
    }
    return render(request,'demo/updatecategory.html',context)

#function to delete the product
@login_required
@admin_only
def product_delete(request,product_id):
    product = Product.objects.get(id = product_id)
    os.remove(product.product_image_url.path)
    product.delete()
    messages.add_message(request,messages.SUCCESS,'Product deleted successfully')
    return redirect('/admin/product')

#function to update product
@login_required
@admin_only
def product_update(request,product_id):
    product = Product.objects.get(id = product_id)
    if request.method == 'POST':
        if request.FILES.get('product_image_url'):
            os.remove(product.product_image_url.path)
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Product updated successfully')
            return redirect('/admin/product')
        else:
            messages.add_message(request,messages.ERROR,'Unable to update product')
            return render(request,'demo/updateproduct.html',{
                'form':form
            })
    context = {
        'form':ProductForm(instance=product)
    }
    return render(request,'demo/updateproduct.html',context)


@login_required
@admin_only
def user_order(request):
    items = Order.objects.all()
    context={
        'items':items
    }
    return render(request,'demo/userorder.html',context)

        
