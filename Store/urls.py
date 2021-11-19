from django.contrib import admin
from django.urls import path
from .views .index import index , singlepage,product_detail


urlpatterns = [
    path('', index , name='indexpage'),
    path('single' , singlepage , name='single'),
    path('product_detail/<int:id>',product_detail , name='product_detail')
]
