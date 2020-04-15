# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from home.models import Contact,Signup,Service
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from math import ceil
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        messages.success(request,'Please Signup first')
        return redirect('login')
    return render(request,'index.html')
def contact(request):
    if request.user.is_anonymous:
        messages.success(request,'Please Signup first')
        return redirect('login')
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        about=request.POST.get('about')
        contact=Contact(name=name,email=email,phone=phone,about=about,date=datetime.today())
        contact.save()
        messages.success(request,'Your message has been sent.')
    return render(request,'contact.html')
def loginUser(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('pass')
        user=authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('index.html')
        else:
            messages.success(request,'Invalid Information')
            return render(request,'login.html')
    return render(request,'login.html')
def about(request):
    if request.user.is_anonymous:
        messages.success(request,'Please Signup first')
        return redirect('login')
    return render(request,'about.html')
def service(request):
    if request.user.is_anonymous:
        messages.success(request,'Please Signup first to Enjoy Our Service')
        return redirect('login')
    allProds=[]
    catProds=Service.objects.values('category','id')
    print(catProds)
    cats={item['category'] for item in catProds }
    print(cats)
    for  cat  in cats:
        prod=Service.objects.filter(category=cat)
        n=len(prod)
        print(prod)
        nSlides=n//4+ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    param={'allProds':allProds}
    return render(request,'service.html',param)
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('first')
        lname=request.POST.get('last')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        if username=='' or fname=='' or lname=='' or email=='' or password=='':
            messages.success(request,'Please Enter Something')
            return redirect(request,'signup.html')
        user=User.objects.create_superuser(username,email,password)
        user.first_name=fname
        user.last_name=lname
        user.save()
        messages.success(request,'SignUP Successfull')
        return redirect('login.html')
    return render(request,'signup.html')
def customer(request):
    return render(request,'Customer.html')
def logoutUser(request):
    logout(request)
    return redirect('login.html')