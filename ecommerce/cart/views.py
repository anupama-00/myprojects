from itertools import product
from lib2to3.fixes.fix_input import context
from locale import currency

import razorpay
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, UpdateView

from shop.models import Product

from cart.models import Cart

from shop.models import Category

from cart.models import Payment, Order_details


# Create your views here.
def addtocart(request,pk):
    u=request.user
    p=Product.objects.get(id=pk)
    try:
        cart=Cart.objects.get(user=u,product=p)
        if p.stock>0:
            cart.quantity+=1
            cart.save()
            p.stock-=1
            p.save()

    except:
        if p.stock:
            cart=Cart.objects.create(user=u,product=p,quantity=1)
            cart.save()
            p.stock-=1
            p.save()

    return redirect('cart:cartview')

def cartview(request):
    u=request.user
    c=Cart.objects.filter(user=u)

    total=0
    for i in c:
        total+=i.quantity*i.product.price
    context={'cart':c,'total':total}
    return render(request,'cart.html',context)

def cartdecrement(request,pk):
    p=Product.objects.get(id=pk)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=p)
        if cart.quantity >1:
            cart.quantity-=1
            cart.save()
            p.stock+=1
            p.save()
        else:
            cart.delete()
    except:
        pass
    return redirect('cart:cartview')

def cartdelete(request,pk):
    p = Product.objects.get(id=pk)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=p)
        cart.delete()
        p.stock=p.stock+cart.quantity
        p.save()

    except:
        pass

    return redirect('cart:cartview')

class Addcategory(CreateView):
    model = Category
    template_name = 'addcategory.html'
    fields = ['name','description','image']
    success_url = reverse_lazy('shop:category')

class Addproduct(CreateView):
    model = Product
    template_name = 'addproducts.html'
    fields = ['name','price','description','stock','category','image']
    success_url = reverse_lazy('shop:category')

class Addstock(UpdateView):
    template_name = 'addstock.html'
    model = Product
    fields = ['stock']
    def get_success_url(self):
        return reverse_lazy('shop:productdetails',kwargs={'pk':self.object.id})

def orderform(request):
    if request.method=="POST":
        a=request.POST['a']
        n=request.POST['n']
        pn=request.POST['p']

        u=request.user
        c=Cart.objects.filter(user=u)

        total=0
        for i in c:
            total+=i.quantity*i.product.price
        total=int(total)

        #razorpay client connection
        client=razorpay.Client(auth=('rzp_test_FF4k4rFOkUXNyJ','ttOf7PtPoj9aTaNGcTDa18RJ'))

        #razorpay order creation
        response_payment=client.order.create(dict(amount=total*100,currency='INR'))
        print(response_payment)
        order_id=response_payment['id']       #retrieve the order id from response
        status=response_payment['status']      #retrieve the status from response
        if status=="created":
            p=Payment.objects.create(name=u.username,amount=total,order_id=order_id)
            p.save()

            for i in c:
                o=Order_details.objects.create(product=i.product,user=i.user,phone=n,address=a,pin=pn,order_id=order_id,no_of_items=i.quantity)
                o.save()

            context={'payment':response_payment,'name':u.username}  #sends the response from view to payment.html

            return render(request,'payment.html',context)

    return render(request,'orderform.html')

@csrf_exempt
def payment_status(request,p):
    user=User.objects.get(username=p)       #retrieve user object
    login(request,user)

    response=request.POST    #razorpay response after successfull payment
    print(response)

    #To check the validity(authenticity) of the razorpay payment details received by application
    param_dict={
    'razorpay_order_id':response.get('razorpay_order_id'),
    'razorpay_payment_id':response.get('razorpay_payment_id'),
    'razorpay_signature':response.get('razorpay_signature')
    }
    client=razorpay.Client(auth=('rzp_test_FF4k4rFOkUXNyJ','ttOf7PtPoj9aTaNGcTDa18RJ'))
    try:
        status=client.utility.verify_payment_signature(param_dict)     #for creating the payment details
        print(status)                                                   #we pass param_dict to verify payment_signature function
        p=Payment.objects.get(order_id=response['razorpay_order_id'])
        p.paid=True
        p.razorpay_payment_id=response['razorpay_payment_id']
        p.save()

        o=Order_details.objects.filter(order_id=response['razorpay_order_id'])
        for i in o:
            i.payment_status="completed"
            i.save()

        c=Cart.objects.filter(user=user)
        c.delete()


    except:
        pass

    return render(request,'payment_status.html')

def your_orders(request):
    u=request.user
    o=Order_details.objects.filter(user=u,payment_status="completed")
    context={'orders':o}
    return render(request,'orders.html',context)