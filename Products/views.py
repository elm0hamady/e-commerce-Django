from django.shortcuts import render
from .models import Product
# Create your views here.
def products(request):
    pro = Product.objects.all()
    pro_filter = {'pro':str(pro.count())}
    return render(request,'Products/products.html',pro_filter)