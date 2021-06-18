from django.contrib import admin
from .models import Order, OrderItem, ShippingAddress, Customer, product


admin.site.register(product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
