from django.contrib import admin
from .models import User,Coupon,Product,FirstPurchaseCoupon
# Register your models here.
admin.site.register(User)
admin.site.register(Coupon)
admin.site.register(Product)
admin.site.register(FirstPurchaseCoupon)