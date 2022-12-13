from django.db import models
from django .contrib.auth .models import User

class slider(models.Model):
    slider = models.ImageField(upload_to = 'upload/slider/img', null=False)
    Show_Slider = models.BooleanField(default=True)

class TshirtProperty(models.Model):
    title = models.CharField(max_length=30, null=False)
    slug = models.CharField(max_length=30, null=False, unique=True)

    def __str__(self):
        return self.title

    # Don't create table in database using this property
    class Meta:
        abstract = True

class Occasion(TshirtProperty):  
    pass

class IdealFor(TshirtProperty):
    pass

class NeckType(TshirtProperty):
    pass

class Sleeve(TshirtProperty):
    pass

class Brand(TshirtProperty):
    pass

class Color(TshirtProperty):
    pass

class Tshirt(models.Model):
    tshirt_name = models.CharField(max_length=100, null=False)
    slug = models.CharField(max_length=200 , null=False , unique=True , default='')
    tshirt_Desc = models.CharField(max_length=100, null=True, blank=True)
    discount = models.IntegerField()
    tshirt_img = models.ImageField(upload_to='upload/img', null=False)
    tshirt_img2 = models.ImageField(upload_to='upload/img', null=True, blank=True)
    tshirt_img3 = models.ImageField(upload_to='upload/img', null=True , blank=True)
    occasion = models.ForeignKey(Occasion, on_delete=models.CASCADE)
    Ideal_for = models.ForeignKey(IdealFor, on_delete=models.CASCADE)
    Neck_type = models.ForeignKey(NeckType, on_delete=models.CASCADE)
    sleeve = models.ForeignKey(Sleeve, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    def __str__(self):
        return self.tshirt_name

class SizeVariant(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    price = models.IntegerField()
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    size = models.CharField(choices=SIZES, max_length=5)

    def __str__(self):
        return f'{self.size}'

class Cart(models.Model):
    sizeVariant = models.ForeignKey(SizeVariant , on_delete=models.CASCADE)
    Quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

class Order(models.Model):
    OrderStatus = (
        ("PENDING" , "Pending"),
        ("PLACED" , "Placed"),
        ("CANCELED" , "Canceled"),
        ("COMPLETE" , "Complete"),
    )

    method = (
        ("COD","Cod"),
        ("ONLINE","Online"),
    )
    order_status = models.CharField(max_length=30, choices=OrderStatus)
    payment_method = models.CharField(max_length=30, choices=method)
    shipping_address = models.CharField(max_length=60 , null=False)
    phone = models.CharField(max_length=10, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(null=False)
    date = models.DateTimeField(null=False , auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    tshirt = models.ForeignKey(Tshirt , on_delete=models.CASCADE)
    size = models.ForeignKey(SizeVariant , on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    date = models.DateTimeField(null=False, auto_now_add=True)

class Payment(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, auto_now_add=True)
    payment_status = models.CharField(max_length=30 , default="FAILED")
    payment_id = models.CharField(max_length=100)
    payment_request_id = models.CharField(max_length=100 , unique=True , null=False)

