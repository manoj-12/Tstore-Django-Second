from django.contrib.auth .forms import UserCreationForm ,AuthenticationForm
from django import forms
from Store .models .product import Order
from django.contrib.auth.models import User


class CheckForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['shipping_address', 'phone' , 'payment_method']
