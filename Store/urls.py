from django.contrib import admin
from django.urls import path
from .views .index import index ,product_detail,addtocart,validate_payment,cart,checkout,order


urlpatterns = [
    path('', index , name='indexpage'),
    path('product_detail/<str:slug>',product_detail , name='product_detail'),
    path('add_to_cart/<str:slug>/<str:size>',addtocart , name='addtocart'),
    path("cart" , cart , name='cart'),
    path('order', order , name='order'),
    path('checkout' , checkout , name="checkout"),
    path('validate_payment' , validate_payment , )
]
