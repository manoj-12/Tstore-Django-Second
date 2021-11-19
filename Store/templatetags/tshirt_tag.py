from math import floor
from django import template

register = template.Library()


@register.simple_tag
def min_price(tshirt):
    size = tshirt.sizevariant_set.all().order_by('price').first() #return min size
    return floor(size.price)


@register.simple_tag
def sale_price(tshirt):
    Price = min_price(tshirt) #return price
    Discount = tshirt.discount #return Discount
    return floor(Price - (Price*Discount/100)) #return sale price

@register.simple_tag
def rupee():
    return f"₹"


@register.simple_tag()
def Active_size_button(active_size , size):
    if active_size == size:
        return "btn-dark"
    else:
        return "btn-light"