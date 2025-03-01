from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from user.models import CustomUser


# Create your views here.
def register(request):
    if request.method=="POST":
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        r=request.POST.get('role')


        if p==cp:
            u=CustomUser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,role=r)
            u.save()
            return redirect('user:login')
        else:
            messages.error(request,"Passwords are not same")

    return render(request,"register.html")


def login_user(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user and user.role=="employee":
            login(request, user)
            return redirect('employee:home')
        elif user and user.role=="recruiter":
            login(request,user)
            return redirect('employee:home')
        else:
            messages.error(request,"Invalid user")
    return render(request,'login.html')

@login_required
def logout_user(request):
    logout(request)
    return redirect('employee:intro')
