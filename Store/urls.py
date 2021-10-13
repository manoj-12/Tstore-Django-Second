from django.contrib import admin
from django.urls import path
from .views .index import index


urlpatterns = [
    path('', index , name='indexpage')
]
