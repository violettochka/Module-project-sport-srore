from django.contrib import admin
from products.models import Products, Purchase, Return
from users.models import User

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')



admin.site.register(Purchase)
admin.site.register(Return)
admin.site.register(Products, ProductsAdmin)
admin.site.register(User)