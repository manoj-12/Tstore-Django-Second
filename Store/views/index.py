from django.shortcuts import render , redirect 
from Store .models .product import  Order ,Tshirt , OrderItem , Payment ,slider , SizeVariant , \
    Cart , Occasion ,Color , IdealFor , Sleeve , NeckType , Brand
from math import floor
from django.contrib.auth.decorators import login_required
from Store .forms .checkout import CheckForm
from instamojo_wrapper import Instamojo
from Eshop .settings import API_KEY , AUTH_TOKEN
API = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');
from django.core.paginator import Paginator
from urllib .parse import urlencode

def index(request):
    Slider = slider.objects.filter(Show_Slider=True)
    data = request.GET
    page = data.get('page')
    if page is None or page == '':
        page = 1
    Brands = data.get('brand')
    Occations = data.get('occation')
    Idealfor = data.get('idealfor')
    sleeves = data.get('sleeve')
    necktypes = data.get('necktype')
    colors = data.get('color')
    occation = Occasion.objects.all()
    brand = Brand.objects.all()
    color = Color.objects.all()
    idealfor = IdealFor.objects.all()
    sleeve = Sleeve.objects.all()
    necktype = NeckType.objects.all()
    tshirt = Tshirt.objects.all()
    if Brands !="" and Brands != None:
        tshirt = tshirt.filter(brand__slug=Brands)
    if Occations !='' and Occations != None:
        tshirt = tshirt.filter(occasion__slug=Occations)
    if  Idealfor !='' and Idealfor != None:
        tshirt = tshirt.filter(Ideal_for__slug=Idealfor)
    if  sleeves !='' and sleeves != None:
        tshirt = tshirt.filter(sleeve__slug=sleeves)
    if necktypes != '' and necktypes != None:
        tshirt = tshirt.filter(Neck_type__slug=necktypes)
    if colors != '' and colors != None:
        tshirt = tshirt.filter(color__slug=colors)
    paginator = Paginator(tshirt , 5)
    page_obj = paginator.get_page(page)

    data = request.GET.copy()
    data['page']=''
    pageurl = urlencode(data)

    context = {
        'occation':occation,
        'brand':brand,
        'color':color,
        'idealfor':idealfor,
        'sleeve':sleeve,
        'necktype':necktype,
        'page_obj':page_obj,
        'Slider':Slider,
        'pageurl':pageurl
    }
    return render(request , 'index.html' , context=context)

def product_detail(request,slug):
    tshirt = Tshirt.objects.get(slug=slug)
    Size = request.GET.get('size')
    
    if Size is None:
        size = tshirt.sizevariant_set.all().order_by('price').first()
    else:
        size = tshirt.sizevariant_set.get(size=Size)
    size_price = size.price #price without discount
    sell_price = size_price - (size_price*(tshirt.discount)/100) #sell Price
    sell_price = floor(sell_price)
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
        c['size'] = SizeVariant.objects.get(tshirt=tshirt_id,size=c['size'])
        c['tshirt'] = tshirt
    context = {
        'cart':cart
    }
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
    
    if user is not None:
        add_cart_database(user , size , tshirt)
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
        size_short = cart_obj.get('size')
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


def clc_total_payable_amount(cart):
    total = 0
    for c in cart:
        dicount = c.get('tshirt').discount
        price = c.get('size').price
        sale_price = floor(price - (price*dicount/100))
        total_of_single_product = sale_price * c.get('Quantity')
        total = total + total_of_single_product
    return total


# @login_required(login_url='/accounts/login')
def order(request):
    user = request.user
    order = Order.objects.filter(user=user).order_by('-date').exclude(order_status='PENDING')
    print(order)
    context = {
        "order":order
    }
    return render(request , 'order.html' , context=context)

@login_required(login_url='/accounts/login')
def checkout(request):
    if request.method == 'GET':
        form = CheckForm()
        cart = request.session.get('cart')
        if cart is None:
            cart = []
        for c in cart:
            size_str = c.get('size')
            tshirt_id = c.get('tshirt')
            size_obj = SizeVariant.objects.get(size=size_str ,tshirt=tshirt_id)
            c['size']=size_obj
            c['tshirt']=size_obj.tshirt 
            context = {
                "checkoutform":form,
                "cart":cart 
            }
        return render(request , 'checkout_form.html' , context=context)

    else:
        form = CheckForm(request.POST)
        user = None
        if request.user.is_authenticated:
            user = request.user
            print("user = :",user)
        if form.is_valid():
            cart = request.session.get('cart')
            if cart is None:
                cart = []
            for c in cart:
                size_str = c.get('size')
                tshirt_id = c.get('tshirt')
                size_obj = SizeVariant.objects.get(size=size_str ,tshirt=tshirt_id)
                c['size']=size_obj
                c['tshirt']=size_obj.tshirt 
            shipping_add = form.cleaned_data.get('shipping_address')
            phone = form.cleaned_data.get('phone')
            payment_method = form.cleaned_data.get('payment_method')
            total = clc_total_payable_amount(cart)
            order = Order()
            order.shipping_address = shipping_add
            order.phone = phone
            order.payment_method = payment_method
            order.total = total
            order.order_status = "PENDING"
            order.user = user
            order.save()

            for c in cart:
                order_item = OrderItem()
                order_item.order = order
                size = c.get('size')
                tshirt = c.get('tshirt')
                order_item.price = floor(size.price-(size.price*tshirt.discount/100))
                order_item.quantity = c.get('Quantity')
                order_item.size = size
                order_item.tshirt = tshirt
                order_item.save()
            

            # Creating Payment
            response = API.payment_request_create(
            amount=order.total,
            purpose='Payment For Tshirt',
            send_email=True,
            buyer_name=f'{user.first_name} {user.last_name}',
            email=user.email,   
            redirect_url="http://localhost:8000/validate_payment"
            )
            print(response['payment_request'])
            payment_request_id=response['payment_request']['id']
            url=response['payment_request']['longurl']

            payment = Payment()
            payment.order = order
            payment.payment_request_id = payment_request_id
            payment.save()
            print(shipping_add , phone, payment_method , total)
            return redirect(url)
        else:
            return redirect('/checkout')


def validate_payment(request):
    user = None
    if request.user.is_authenticated:
        user = request.user
    payment_request_id = request.GET.get('payment_request_id')
    payment_id = request.GET.get('payment_id')
    print('patment Request Id =:',payment_request_id , "payment id =:", payment_id)
    response = API.payment_request_payment_status(payment_request_id,payment_id)
    status = response.get('payment_request').get('payment').get('status') # Payment status 
    print(status)   
    if status != 'Failed':
        try:
            payment = Payment.objects.get(payment_request_id=payment_request_id)
            payment.payment_id = payment_id
            payment.payment_status = status  
            payment.save()
            order = payment.order
            order.order_status = 'PLACED'
            order.save()
            cart = []
            request.session['cart']=cart
            Cart.objects.filter(user=user).delete()
            return redirect("order")
        except:
            return render(request ,  'payment_failed.html')
    # return render(request ,  'payment_failed.html')