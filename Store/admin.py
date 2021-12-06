from django.contrib import admin
from Store .models .product import Occasion , \
    Sleeve , NeckType , Brand , \
    Color , IdealFor  ,Tshirt , SizeVariant , \
    slider , Cart , Order , OrderItem , Payment
# Register your models here.


class SizeVariantConfig(admin. TabularInline): #1.TabularInline 2.StackedInline
    model = SizeVariant # First Make SizeVariant TabularInline


class TshirtConfig(admin.ModelAdmin):
    inlines = [SizeVariantConfig] #Where is Apply Inline Method
    list_display = ['tshirt_name','brand','Ideal_for','occasion','Neck_type','sleeve','color' , 'slug']



class SizeVariantAdmin(admin.ModelAdmin):
    list_display = ['size','price']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['tshirt','size','quantity','price']

admin.site.register(Tshirt , TshirtConfig) #pass class
admin.site.register(Occasion)
admin.site.register(Sleeve)
admin.site.register(NeckType)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(IdealFor)
admin.site.register(slider)
admin.site.register(Cart)
admin.site.register(SizeVariant)
admin.site.register(Order)
admin.site.register(OrderItem , OrderItemAdmin)
admin.site.register(Payment)
