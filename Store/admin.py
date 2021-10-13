from django.contrib import admin
from Store .models .product import Occasion , \
    Sleeve , NeckType , Brand , \
    Color , IdealFor  ,Tshirt , SizeVariant
# Register your models here.


class SizeVariantConfig(admin. TabularInline): #1.TabularInline 2.StackedInline
    model = SizeVariant # First Make SizeVariant TabularInline


class TshirtConfig(admin.ModelAdmin):
    inlines = [SizeVariantConfig] #Where is Apply Inline Method







admin.site.register(Tshirt , TshirtConfig) #pass class
admin.site.register(Occasion)
admin.site.register(Sleeve)
admin.site.register(NeckType)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(IdealFor)
# admin.site.register(SizeVariant)
