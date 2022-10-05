from tkinter import N
from django.contrib import admin
from django.urls import path

from store.models import Wishlist
from . import views
from store.controller import authview,cart,wishlist,checkout,order


urlpatterns = [
    path('',views.home,name='home'),
    path('collections',views.collections,name="collections"),
    path('collections/<str:slug>',views.collectionsview,name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productsview,name='productsview'),
    path('product-list',views.productlistAjax),
    path('searchproduct',views.searchproduct,name='searchproduct'),

    path('register/',authview.register,name='register'),
    path('login/',authview.loginweb,name='loginweb'),
    path('logout/',authview.logoutweb,name='logoutweb'),

    path('add-to-cart',cart.addtocart,name='addtocart'),
    path('cart',cart.viewcart,name='cart'),
    path('update-cart',cart.updatecart,name='updatecart'),
    path('delete-cart-item', cart.deletecartitem,name='deletecartitem'),

    path('wishlist',wishlist.index,name='wishlist'),
    path('add-to-wishlist',wishlist.addtowishlist,name='addtowishlist'),
    path('delete-wishlist-item',wishlist.deletewishlistitem,name='deletewishlistitem'),

    path('checkout',checkout.index,name='checkout'),
    path('place-order',checkout.placeorder,name='placeorder'),
    path('proceed-to-pay',checkout.razorpaycheck),

    path('my-orders',order.index,name='myorders'),
    path('orderview/<str:t_no>',order.vieworder,name='orderview')
    
    
]
