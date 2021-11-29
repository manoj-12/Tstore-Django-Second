from django.contrib import admin
from django.urls import path
from .views .index import index , singlepage, product_detail,addtocart,cart,checkout


urlpatterns = [
    path('', index , name='indexpage'),
    path('single' , singlepage , name='single'),
    path('product_detail/<str:slug>',product_detail , name='product_detail'),
    path('add_to_cart/<str:slug>/<str:size>',addtocart , name='addtocart'),
    path("cart" , cart , name='cart'),
    path('checkout' , checkout , name="checkout")
]
