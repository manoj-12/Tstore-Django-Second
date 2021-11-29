from django.contrib import admin
from django.urls import path
from accounts .views import register , login , LogOut

urlpatterns = [
    path('register', register , name='register'),
    path('login',login , name='login'),
    path('LogOut' , LogOut , name='LogOut')
]
