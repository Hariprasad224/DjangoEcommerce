from django.contrib import admin

from store.models import Cart, Category, OrderItem, Product,Order, Profile
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)