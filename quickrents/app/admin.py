from django.contrib import admin
from .models import (
    Car,
    Customer,
    My_Order,
    OrderPlaced
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Car)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','renting_price','description','brand','category','car_image']

@admin.register(My_Order)
class My_OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','car','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user', 'customer', 'car', 'quantity', 'status']
