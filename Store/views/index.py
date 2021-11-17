from django.shortcuts import render
from Store .models .product import IdealFor ,Tshirt , slider

def index(request):
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
    print(idea_for_id)
    tshirt = Tshirt.objects.filter(Ideal_for=idea_for_id)
    # print('Ideal For ',Ideal_For)
    context = {
        'Ideal_For':Ideal_for,
        'tshirt':tshirt
    }
    return render(request ,'single.html',context=context)


def product_detail(request):
    return render(request,'product_detail.html')