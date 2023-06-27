"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from home.views import *
from product.views import (
    product_list,
    product_detail,
    product_create,
    product_update,
    product_delete,
)

urlpatterns = [
    path('',home, name="home"),
    path('account',include('accounts.urls')),#connecting to account



    path('success/page',success_page, name="success_page"),
    path('admin/', admin.site.urls),

    path('product', product_list, name='product_list'),
    path('product/create/', product_create, name='product_create'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/<int:pk>/update/', product_update, name='product_update'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
]
