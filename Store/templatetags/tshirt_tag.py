from math import floor
from django import template
register = template.Library()

@register.filter
def clc_total_payable_amount(cart):
    total = 0
    for c in cart:
        dicount = c.get('tshirt').discount
        price = c.get('size').price
        sale_price = clc_sale_price(price,dicount)
        total_of_single_product = sale_price * c.get('Quantity')
        total = total + total_of_single_product
    return total

@register.simple_tag
def min_price(tshirt):
    size = tshirt.sizevariant_set.all().order_by('price').first() #return min size
    return floor(size.price)

@register.simple_tag
def clc_sale_price(price,discount):
    return floor( price- (price * discount / 100))

@register.simple_tag
def sale_price(tshirt):
    Price = min_price(tshirt) #return price
    Discount = tshirt.discount #return Discount
    return floor(Price - (Price*Discount/100)) #return sale price

@register.simple_tag
def multiply(a,b):
    return a*b

@register.simple_tag
def rupee():
    return f"₹"

@register.simple_tag
def Active_size_button(active_size , size):
    if active_size == size:
        return "btn-dark"
    else:
        return "btn-light"

@register.simple_tag
def selected_attr(request_slug , slug):
    if (request_slug == slug):
        return 'selected'
    else:
        return ''


