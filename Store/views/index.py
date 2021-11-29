from django.shortcuts import render , redirect , HttpResponse
from Store .models .product import IdealFor ,Tshirt , slider , SizeVariant , Cart
from math import floor

from django.contrib.auth.decorators import login_required
from Store .forms .checkout import CheckForm

def index(request):
    cart = request.session.get("cart")
    print(cart)
    Slider = slider.objects.filter(Show_Slider=True)
    # print('Slider',Slider)
    tshirt = Tshirt.objects.filter(Add_Home_Page=True).order_by("-id")
    # for t in tshirt:
    #     min_price = t.sizevariant_set.all().order_by('price').first()
    #     print('Min Size = ',min_price) #found Min Size
    #     t.min_price = min_price.price
    #     # t.id = t.id
    #     # print('Id = ', t.id) # tshirt id found
    #     print('Tshirt Price = ',t.min_price) # Found Min Price
    #     t.after_discount = t.min_price - (t.min_price * t.discount/100)
    #     t.after_discount = floor(t.after_discount)
    #     print(t.tshirt_name,min_price.price , min_price.size)
       
         

    Ideal_For = IdealFor.objects.all()
    context = {
        'Ideal_For':Ideal_For,
        'tshirt':tshirt,
        'Slider':Slider
    }

    return render(request , 'index.html' , context=context)

def singlepage(request):
    Ideal_for = IdealFor.objects.all()
    idea_for_id= request.GET.get("idealfor")
    # print(idea_for_id)
    tshirt = Tshirt.objects.filter(Ideal_for=idea_for_id)
    # print('Ideal For ',Ideal_For)
    context = {
        'Ideal_For':Ideal_for,
        'tshirt':tshirt
    }
    return render(request ,'single.html',context=context)

def product_detail(request,slug):
    # tshirt = Tshirt.objects.filter(id=TshirtID)
    tshirt = Tshirt.objects.get(slug=slug)
    # print("Tshirt ID =:",tshirt.id)
    Size = request.GET.get('size')
    # print("Size =:",Size)
    if Size is None:
        size = tshirt.sizevariant_set.all().order_by('price').first()
    else:
        size = tshirt.sizevariant_set.get(size=Size)
    size_price = size.price #price without discount
    sell_price = size_price - (size_price*(tshirt.discount)/100) #sell Price
    sell_price = floor(sell_price)
    # print(size.size)
    # print("Price =:",size.price)
    # print("Tshirt Name =:",tshirt.tshirt_name)
    context = {
        'tshirt':tshirt,
        'size_price':size_price,
        'sell_price':sell_price,
        'active_size': size

    }
    return render(request,'product_detail.html', context=context)
'''cart page '''
def cart(request):
    cart = request.session.get('cart')
    if cart is None:
        cart = []
    for c in cart:
        tshirt_id = c.get('tshirt')
        tshirt = Tshirt.objects.get(id=tshirt_id)
        print(tshirt.tshirt_name)
        c['size'] = SizeVariant.objects.get(tshirt=tshirt_id,size=c['size'])
        c['tshirt'] = tshirt
    context = {
        'cart':cart
    }
    print(cart)
    return render(request , "cart.html" , context=context)
'''End cart page '''

'''add to cart manage '''
def addtocart(request , slug ,size):
    user = None
    if request.user.is_authenticated:
        user = request.user
    cart = request.session.get('cart') #supposed session in cart
    if cart is None:
        cart = []
    tshirt = Tshirt.objects.get(slug=slug)
    add_cart_for_anom_user(cart, size , tshirt)
    '''
    temp_size = SizeVariant.objects.get(size = size , tshirt = tshirt)
    flag = True
    for cart_obj in cart:
        t_id = cart_obj.get('tshirt')
        # temp_size = cart_obj.get('size')
        size_short = cart_obj.get('size')
        # if t_id == tshirt.id and temp_size==size:
        if t_id == tshirt.id and size==size_short:
            flag = False
            cart_obj['Quantity'] = cart_obj['Quantity']+1

    if flag:
        cart_obj = {
            'tshirt': tshirt.id,
            'size': size,
            'Quantity': 1
        }
        cart.append(cart_obj)
        '''
    if user is not None:
        add_cart_database(user , size , tshirt)
        '''
            FOR PRACTICE
            existing = Cart.objects.filter(user=user , sizeVariant = temp_size )
            if len(existing) > 0:
                obj = existing[0]
                obj.Quantity = obj.Quantity+1
                obj.save()
            else:
                c = Cart()
                c.user = user
                c.sizeVariant = temp_size
                c.Quantity = 1
                c.save()
        '''
    request.session['cart']=cart #create session assign the value of cart
    return_url = request.GET.get("return_url")
    return redirect(return_url)

def add_cart_database(user, size , tshirt):
    size = SizeVariant.objects.get(size=size, tshirt=tshirt)
    existing = Cart.objects.filter(user=user, sizeVariant=size)
    if len(existing) > 0:
        obj = existing[0]
        obj.Quantity = obj.Quantity + 1
        obj.save()
    else:
        c = Cart()
        c.user = user
        c.sizeVariant = size
        c.Quantity = 1
        c.save()

def add_cart_for_anom_user(cart , size , tshirt):
    flag = True
    for cart_obj in cart:
        t_id = cart_obj.get('tshirt')
        # temp_size = cart_obj.get('size')
        size_short = cart_obj.get('size')
        # if t_id == tshirt.id and temp_size==size:
        if t_id == tshirt.id and size == size_short:
            flag = False
            cart_obj['Quantity'] = cart_obj['Quantity'] + 1

    if flag:
        cart_obj = {
            'tshirt': tshirt.id,
            'size': size,
            'Quantity': 1
        }
        cart.append(cart_obj)

'''End cart manage '''

@login_required(login_url='/accounts/login')
def checkout(request):
    form = CheckForm()
    return render(request , 'checkout_form.html' , {"checkoutform":form})


