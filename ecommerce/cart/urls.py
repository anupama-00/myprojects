"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from cart import views

app_name='cart'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:pk>',views.addtocart,name="addtocart"),
    path('cartdecrement/<int:pk>',views.cartdecrement,name="cartdecrement"),
    path('cartdelete/<int:pk>',views.cartdelete,name="cartdelete"),
    path('cartview',views.cartview,name="cartview"),
    path('addcategory',views.Addcategory.as_view(),name="addcategory"),
    path('addproduct',views.Addproduct.as_view(),name="addproduct"),
    path('addstock/<int:pk>',views.Addstock.as_view(),name="addstock"),
    path('orderform',views.orderform,name="orderform"),
    path('payment_status/<p>',views.payment_status,name="payment_status"),
    path('orders',views.your_orders,name="orders"),

]

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)