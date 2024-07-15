from django.contrib import admin
from .models import Order, ItemOrder

class ItemOrderInLine(admin.TabularInline):
    model = ItemOrder
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ItemOrderInLine, 
    ]
    
admin.site.register(Order, OrderAdmin)
admin.site.register(ItemOrder)
