from django.shortcuts import HttpResponse
from math import prod
from multiprocessing import context
from tokenize import Pointfloat
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from store.controller.checkout import orders
from store.models import Order, OrderItem
from django.contrib.auth.decorators import login_required

def index(request):
    orders = Order.objects.filter(user = request.user)
    context = {'orders' : orders}
    return render(request,'products/order.html',context)

def vieworder(request,t_no):
    order = Order.objects.filter(tracking_no = t_no).filter(user=request.user).first()
    orderitems = OrderItem.objects.filter(order = order)
    context = {'order': order, 'orderitems': orderitems}
    return render(request,'products/orderview.html',context)