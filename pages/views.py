from django.shortcuts import render
from .models import Creds
from .forms import Credentials
# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def about(request):
    pass

def cred(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        data = Creds(username=username,password=password)
        # if data.is_valid():
        data.save()


    return render(request,'pages/login.html',{'creds':Credentials})