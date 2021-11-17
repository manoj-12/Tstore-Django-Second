from django.contrib.auth import forms
from django.shortcuts import render, redirect
from accounts .form .authyform import CustomerCreationForm,CustomerAuthForm
from django.contrib.auth import authenticate , login as loginUser,logout
# Create your views here.

def register(request):
    if request.method == 'GET':
        print('method Get =',request.method)
        form = CustomerCreationForm
        context = {
            'form':form
            }
        return render(request , 'registerform.html' , context=context)
    else:
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()
            return redirect('login')
        else:
            context = {
                'form':form
            }
            return render(request , 'registerform.html' , context=context)

def login(request):
    if request.method == 'GET':
        form = CustomerAuthForm
        return render(request, 'login.html' ,{'form':form})
    else:
        form =  form = CustomerAuthForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user:
                loginUser(request,user) # session ko manage karne k liye login method ko call krna jaruri hota h aur esame object pass karna bhi 
                return redirect('/')
        else:
            return render(request, 'login.html' ,{'form':form})


def LogOut(request):
    logout(request) # it is method all ready created by django
    # request.session.clear()
    return redirect('/')