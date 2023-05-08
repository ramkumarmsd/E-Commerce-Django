from django.shortcuts import render,redirect
from .models import *
from .form import forms
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json

# Create your views here.

def home(request):
    data = category.objects.filter(status=0)
    return render(request,'home.html',{'datas':data})

def products(request,pname):
    if category.objects.filter(name=pname,status=0):
        datas = product.objects.filter(catagory__name=pname)
    return render(request,'product.html',{'datas':datas ,'pname':pname})    

def productview(request,cname,name):
    if category.objects.filter(name=cname,status=0):
        if product.objects.filter(name=name,status=0):
            datas = product.objects.filter(name=name).first()
            return render(request,'productview.html',{'datas':datas})    

def trending(request):
    trend = product.objects.filter(trending=1)
    return render(request,'trending.html',{'trend':trend})

def register(request):
    form = forms()
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        if request.method == "POST":
            form = forms(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Registered successfull...!!!")
                return redirect('login')
    return render(request,'register.html',{'form':form})

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == "POST":
            name = request.POST.get("username")
            pwd = request.POST.get("password")
            user = authenticate(username=name,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid password or username...!!!")
                return redirect('login')
    return render(request,'login.html') 

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')

def carts(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qtn = data['product_qtn']
            product_id = data['pid']
            product_status = product.objects.get(id=product_id)
            if product_status:
              if cart.objects.filter(user=request.user.id, products_id = product_id):
                return JsonResponse({'status':'Product already in cart'},status=200)
              else:
                if product_status.quantity>=product_qtn:
                    cart.objects.create(user=request.user, products_id=product_id, product_qtn=product_qtn)
                    return JsonResponse({'status':'product added to cart'},status=200)
                else:
                    return JsonResponse({'status':'product stock not available'},status=200)
        else:
           return JsonResponse({'status': 'Login to Add cart '} ,status=200)
    else:
        return JsonResponse({'status': 'Invalid access'} ,status=200)
    
def cart_page(request):
    if request.user.is_authenticated:
        datas = cart.objects.filter(user=request.user)
        return render(request,'cart.html',{'datas':datas})
    else:
        return render(request,'cart.html')
    
def remove_cart(request,cid):
    carts= cart.objects.get(id=cid)
    carts.delete()
    return redirect('cart_page')

def favourites(request):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if request.user.is_authenticated:
                data = json.load(request)
                product_id = data['pid']
                product_status = product.objects.get(id=product_id)
                if product_status:
                    if favourite.objects.filter(user=request.user.id, products_id = product_id):
                        return JsonResponse({'status':'Product already in favourite'},status=200)
                    else:
                        favourite.objects.create(user=request.user, products_id=product_id)
                        return JsonResponse({'status':'product added to favourite'},status=200)
            else:
                return JsonResponse({'status': 'Login to Add favourite '} ,status=200)
        else:
            return JsonResponse({'status': 'Invalid access'} ,status=200)  
   

def favourite_page(request):
    if request.user.is_authenticated:
        datas = favourite.objects.filter(user=request.user)
        return render(request,'favourite.html',{'datas':datas})
    else:
        return render(request,'favourite.html')
    
def remove_fav(request,fid):
    fav = favourite.objects.get(id=fid)
    fav.delete()
    return redirect('favourite_page')


