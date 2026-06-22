from django.shortcuts import render
from .models import Producta
# Create your views here.
def products(request):
    pro = Producta.objects.all()
    pro_filter = {'pro':pro.order_by('created_at')}
    return render(request,'Products/products.html',pro_filter)