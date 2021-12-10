from typing import List
from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from Store .models .product import Occasion , \
    Sleeve , NeckType , Brand , \
    Color , IdealFor  ,Tshirt , SizeVariant , \
    slider , Cart , Order , OrderItem , Payment
# Register your models here.


class SizeVariantConfig(admin. TabularInline): #1.TabularInline 2.StackedInline
    model = SizeVariant # First Make SizeVariant TabularInline


class TshirtConfig(admin.ModelAdmin):
    inlines = [SizeVariantConfig] #Where is Apply Inline Method
    list_display = ['id','get_tshirt_img','tshirt_name','brand','Ideal_for','occasion','Neck_type','sleeve','color' ,'discount']
    list_editable = ['discount']

    def get_tshirt_img(self , obj):
        return format_html(f"""

        <a target='_blank' href='{obj.tshirt_img.url}'><img height='50px' src='{obj.tshirt_img.url}'/></a>

        """)

class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size','price']


class OrderitemAdmin(admin. TabularInline):
    model =  OrderItem
   
class PaymentAdmin(admin.TabularInline):
    model = Payment



  

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['tshirt','size','quantity','price']


class CartAdmin(admin.ModelAdmin):
    
    list_display=['Quantity','sizeVariant','tshirt','First_Name','Last_Name']
    
    fieldsets = (
        ('Cart Info ', {"fields": ('user','get_tshirt','get_sizeVariant','Quantity', ) } ),
    )

    readonly_fields = ('user','get_sizeVariant','get_tshirt','Quantity',)

    def get_tshirt(self , obj):
        tshirt = obj.sizeVariant.tshirt
        tshirt_id = tshirt.id
        name = tshirt.tshirt_name
        return format_html(f'<a href="/admin/Store/tshirt/{tshirt_id}/change/" target ="_blank">{name}</a>')

    get_tshirt.short_description ="Tshirt"

    def get_sizeVariant(self , obj):
        return obj.sizeVariant  

    get_sizeVariant.short_description = "Size"

    def tshirt(self , obj):
        return obj.sizeVariant.tshirt.tshirt_name

    def First_Name(self , obj):
        return obj.user.first_name

    def Last_Name(self , obj):
        return obj.user.last_name    



class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','shipping_address','payment_method','phone','date','order_status','firstname']

    inlines = [PaymentAdmin,OrderitemAdmin ]
    # fieldsets = ('Order Info' , {'fields':('user','shipping_address','payment_method','phone','order_status',)}),


    readonly_fields = ('user','shipping_address','phone','total','payment_method',)
    def firstname(self , obj):

        
        return obj.user.first_name






















admin.site.register(Tshirt , TshirtConfig) #pass class
admin.site.register(Occasion)
admin.site.register(Sleeve)
admin.site.register(NeckType)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(IdealFor)
admin.site.register(slider)
admin.site.register(Cart , CartAdmin)
admin.site.register(SizeVariant , SizeVariantAdmin)
admin.site.register(Order , OrderAdmin)
admin.site.register(OrderItem , OrderItemAdmin)
admin.site.register(Payment)
