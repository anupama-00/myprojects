"""
URL configuration for jobproject project.

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
from tkinter.font import names

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from employee import views
app_name='employee'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.intro,name="intro"),
    path('home',views.home,name='home'),
    path('applyjob/<int:pk>',views.applyjob,name='applyjob'),
    path('success',views.success,name='success'),
    path('intro',views.intro,name="intro"),
    path('search',views.search,name="search"),
    path('myjobs',views.myjobs, name='myjobs'),
    path('save-job/<int:pk>/', views.save_job, name='save_job'),
    path('saved_jobs',views.saved_jobs, name='saved_jobs'),
path('remove/<int:pk>/', views.remove, name='remove'),


]

