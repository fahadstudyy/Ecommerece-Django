from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import Order, OrderItem, Customer, product
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, login, authenticate
from django.db import IntegrityError



def home(request):
    products = product.objects.all()
    return render(request, 'ecommerece\home.html', {'products': products})

def product_detail(request, product_id):
    details = get_object_or_404(product, pk=product_id)
    return render(request, 'ecommerece/product_detail.html', {'details': details})

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        result = product.objects.filter(name__contains = searched)
        return render(request, 'ecommerece/search.html', {'searched': searched ,'result':result})
    else:
        return render(request, 'ecommerece/search.html', {})
    
def signups(request):
    if request.method == 'GET': 
        return render(request,'ecommerece/signup.html', {'form': UserCreationForm})
    else:
        try:
            if request.POST['password1'] == request.POST['password2']:    
                user = User.objects.create_user(username = request.POST['username'],password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')

        except IntegrityError:
            return render(request,'ecommerece/signup.html', {'form': UserCreationForm, 'exist': 'The user You Enter Already Exist'})
                
        else:
            return render(request,'ecommerece/signup.html', {'form': UserCreationForm, 'mismatch': 'Password mismatch.'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'ecommerece/signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'ecommerece/signin.html', {'form': AuthenticationForm, 'error': 'User not found'})
        else:
            login(request, user)
            return redirect('home')

def about(request):
    return render(request, 'ecommerece/about.html', {'show': 'Its about'})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0} 
    return render(request, 'ecommerece/cart.html',{'items': items, 'order': order})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}    
    return render(request, 'ecommerece/checkout.html', {'items': items, 'order': order})

    
def shop(request):
    return render(request, 'ecommerece/shop.html', {'show': 'Its a checkout'})