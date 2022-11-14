# from django.shortcuts import render
# from .models import *

from math import prod
from django.shortcuts import render
from.models import*
from django.core.exceptions import ObjectDoesNotExist
# from core.models import products
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
#paginator


from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
# Create your views here.
def Login(request):
    return render(request,'login.html')

#Home page
def index(request):
    return render(request,'index.html')

#Register
def register(request):
    return render(request,'register.html')

#product
def product(request,c_slug=None):

    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(Categ, slug=c_slug)
        prodt = Products.objects.filter(category=c_page, available=True)
    else:
        prodt = Products.objects.all().filter(available=True)
    cat = Categ.objects.all()

    product=Products.objects.all()
    pag = Paginator(Products.objects.all(),8)
    page = request.GET.get('page')
    venues = pag.get_page(page)
    context={
        'product':product,
        'product':venues,
        'pr': prodt,
        'ct':cat
      
        }
    return render(request,'products.html',context)

# def pro(request):
#     return render(request,'Profducts.html')

#contact
def contact(request):
    return render(request,'contact.html')

def product_views(request,c_slug,product_slug):
    try:
        prod=Products.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e

    return render(request,'shop-single.html', {'product':prod})


#Cart
def cart(request):
    return render(request,'cart.html')


#cart
def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def cartdetails(request, tot=0, count=0, c=0,c_item=None):
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
        c_item = CartItems.objects.filter(cart=ct, active=True)
        for i in c_item:
            tot += (i.prod.price * i.quan)
            c = c + 1
        count = tot + 100
    except ObjectDoesNotExist:
        pass
    context= {
        'ci': c_item,
        't': tot,
        'cn': count,
        'c': c
        }
    return render(request, 'cart.html',context)


def add_cart(request, product_id):
    pro = Products.objects.get(id=product_id)
    try:
        ct = CartList.objects.get(cart_id=c_id(request))
    except CartList.DoesNotExist:
        ct = CartList.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        ct_item = CartItems.objects.get(prod=pro, cart=ct)
        if ct_item.quan < ct_item.prod.stock:
            ct_item.quan += 1
        ct_item.save()
    except CartItems.DoesNotExist:
        ct_item = CartItems.objects.create(prod=pro, quan=1, cart=ct)
        ct_item.save()
    return redirect('cart_Details')


def min_cart(request, product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    pro = get_object_or_404(Products, id=product_id)
    c_item = CartItems.objects.get(prod=pro, cart=ct)
    if c_item.quan > 1:
        c_item.quan -= 1
        c_item.save()
    else:
        c_item.delete()

    return redirect('cart_Details')

def remove(request,product_id):
    ct = CartList.objects.get(cart_id=c_id(request))
    pro = get_object_or_404(Products, id=product_id)
    c_item = CartItems.objects.get(prod=pro, cart=ct)
    c_item.delete()
    return redirect('cart_Details')