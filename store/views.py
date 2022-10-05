from cgi import print_directory
from itertools import product
from multiprocessing import context
from django.contrib import messages
from unicodedata import category
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Category,Product

# Create your views here.
def home(request):
    return render(request,'index.html')

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category' : category }
    return render(request,'collections.html',context)

def collectionsview(request,slug):
    if Category.objects.filter(slug=slug, status=0):
        product = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'product':product,'category':category}
        return render(request,'products/index.html',context)
    else:
        messages.warning(request,"No such category found")
        return redirect('collections')

def productsview(request,cate_slug,prod_slug):
    if Category.objects.filter(slug=cate_slug, status=0):
        if Product.objects.filter(slug=prod_slug, status=0):
            product =Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'product':product}

        else:
            messages.error(request,"No such product found")
            return redirect('collections')

    else:
        messages.error(request,"No such category found")
        return redirect('collections')
    return render(request,'products/view.html',context)

def productlistAjax(request):
    products = Product.objects.filter(status = 0).values_list('name', flat=True)
    productlist = list(products)

    return JsonResponse(productlist,safe = False)

def searchproduct(request):
    if request.method == 'POST':
        searchterm = request.POST.get('productsearch')
        if searchterm == "":
            return redirect(request.META.get('HTTP_REFERER'))

        else:
            product = Product.objects.filter(name__contains = searchterm).first()

            if product:
                return redirect('collections/'+product.category.slug +'/'+product.slug)
            else:
                messages.info(request, "No product found")
                return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))