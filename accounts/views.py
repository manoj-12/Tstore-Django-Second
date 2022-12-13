from django.contrib.auth import forms
from django.shortcuts import render, redirect
from accounts .form .authform import CustomerCreationForm,CustomerAuthForm
from django.contrib.auth import authenticate , login as loginUser,logout
from Store .models .product import Cart , SizeVariant
# Create your views here.

def register(request):
    if request.method == 'GET':
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
        next_page = request.GET.get('next')
        if next_page is not None:
            request.session['next_page'] = next_page
        return render(request, 'login.html' ,{'form':form})
    else:
        form = CustomerAuthForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            if user:
                loginUser(request,user) # session ko manage karne k liye login method ko call krna jaruri hota h aur esame object pass karna bhi
                #{ size , thirt , quantity }
                session_cart = request.session.get('cart')
                if session_cart is None:
                    session_cart = []
                else:
                    for c in session_cart:
                        size = c.get('size')
                        tshirt_id = c.get('tshirt')
                        quantity = c.get('quantity')
                        cart_obj = Cart()
                        cart_obj.sizeVariant = SizeVariant.objects.get(size=size , tshirt=tshirt_id)
                        cart_obj.quantity = quantity
                        cart_obj.user = user
                        cart_obj.save()
                cart = Cart.objects.filter(user = user)
                session_cart = []
                for c in cart:
                    obj = {
                        'size':c.sizeVariant.size,
                        'tshirt':c.sizeVariant.tshirt.id,
                        'Quantity':c.Quantity
                    }
                    session_cart.append(obj)
                request.session['cart'] = session_cart
                next_page = request.session.get('next_page')
                if next_page is None:
                    next_page = '/'
                return redirect(next_page)
        else:
            return render(request, 'login.html' ,{'form':form})

def LogOut(request):
    logout(request) # it is method all ready created by django
    # request.session.clear()
    return redirect('/')