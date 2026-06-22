from django.contrib import admin
from .models import User,Coupon,Product,FirstPurchaseCoupon,Creds
# from .forms import Credentials
# Register your models here.
admin.site.register(User)
admin.site.register(Coupon)
admin.site.register(Product)
admin.site.register(FirstPurchaseCoupon)
admin.site.register(Creds)
# admin.site.register(Credentials)