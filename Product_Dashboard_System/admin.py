from django.contrib import admin
from .models import Product, Order, ItemOrder


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'name', 'price'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = 'name_client', 'email_client', 'phone_number'


@admin.register(ItemOrder)
class ItemOrderAdmin(admin.ModelAdmin):
    list_display = 'order', 'product', 'quantity'
