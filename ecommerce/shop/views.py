

from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages

from shop.models import Category,Product

from shop.forms import RegisterForm


# Create your views here.
class Categorylist(ListView):
    model=Category
    template_name = 'category.html'
    context_object_name = 'category'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('shop:login')  # Redirect to login page
        return super().dispatch(request, *args, **kwargs)


class Productlist(DetailView):
    model=Category
    template_name = 'products.html'
    context_object_name = 'products'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('shop:login')  # Redirect to login page
        return super().dispatch(request, *args, **kwargs)


class Allproducts(ListView):
    model=Product
    template_name = 'allproducts.html'
    context_object_name = 'allproducts'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('shop:login')  # Redirect to login page
        return super().dispatch(request, *args, **kwargs)


class Productdetails(DetailView):
    model = Product
    template_name = 'productdetails.html'
    context_object_name = 'productdetails'
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('shop:login')  # Redirect to login page
        return super().dispatch(request, *args, **kwargs)


class Register(CreateView):
    template_name = 'register.html'
    model = User
    # fields = ['username','password','email','first_name','last_name']
    form_class = RegisterForm
    success_url = reverse_lazy('shop:login')

    def form_valid(self, form):
        u=form.cleaned_data['username']
        p=form.cleaned_data['password']
        cp=form.cleaned_data['confirm_password']
        e = form.cleaned_data['email']
        f = form.cleaned_data['first_name']
        l = form.cleaned_data['last_name']
        if p==cp:
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return redirect('shop:login')
        else:
            messages.error(self.request,"Passwords doesn't match")
            return redirect('shop:register')



class Login(LoginView):
    template_name = 'login.html'


class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('shop:category')
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('shop:login')  # Redirect to login page
        return super().dispatch(request, *args, **kwargs)

