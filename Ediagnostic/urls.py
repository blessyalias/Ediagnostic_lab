"""
URL configuration for Ediagnostic project.

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
from django.urls import path
from EdiagApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Index),
    path('login',views.login),
    path('client_reg',views.client_reg),
    path('lab_reg',views.lab_reg),

    path('admin_home',views.admin_home),
    path('admin_client',views.admin_client),
    path('admin_lab',views.admin_lab),
    path('admin_action',views.admin_action),
    path('admin_tests',views.admin_tests),
    path('admin_orders',views.admin_orders),
    path('admin_payments',views.admin_payments),
    path('adm_bookedTets',views.adm_bookedTets),

    path('lab_home',views.lab_home),
    path('lab_tests',views.lab_tests),
    path('labDelTest',views.labDelTest),
    path('lab_slots',views.lab_slots),
    path('lab_completed',views.lab_completed),
    path('lab_addReport',views.lab_addReport),
    path('lab_bookedTets',views.lab_bookedTets),

    path('user_home',views.user_home),
    path('user_labs',views.user_labs),
    path('user_slots',views.user_slots),
    path('user_bookslot',views.user_bookslot),
    path('user_bookings',views.user_bookings),
    path('user_tests',views.user_tests),
    path('user_pay',views.user_pay),
    path('user_payments',views.user_payments),
    path('user_bookedTets',views.user_bookedTets),
    path('user_predict',views.user_predict),
    path('print_res',views.print_res),
    path('user_history',views.user_history),
]
