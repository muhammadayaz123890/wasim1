from django.contrib import admin
from .models import *


class Product_Admin(admin.ModelAdmin):


    list_display = ['title','category', 'price', 'quantity']
    search_fields = ['title', 'category', 'price', 'quantity']




admin.site.site_title = "Admin Site"

admin.site.register(Product, Product_Admin)
@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'is_allowed', 'is_active')
    list_filter = ('is_allowed', 'is_active')
    search_fields = ('user__username', 'first_name', 'last_name', 'business_title')
