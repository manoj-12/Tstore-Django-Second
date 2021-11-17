
from django.db import models

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
    Add_Home_Page = models.BooleanField(default=True)




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
        return self.size