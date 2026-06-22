from django.db import models

# Create your models here.

class Creds(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
#relations


#ManyToMany
class Product(models.Model):
    title = models.TextField(max_length=40)
    def __str__(self):
        return self.title
    
#OneToMany 
class FirstPurchaseCoupon(models.Model):
    code = models.TextField(max_length=40)

class User(models.Model):
    gender_type = [
        ('male','male'),
        ('female','female')
    ]
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10,choices=gender_type)
    #ManyToMany
    products = models.ManyToManyField(Product,blank=True)
    #OneToMany 
    first_purchase_code = models.ForeignKey(FirstPurchaseCoupon,on_delete=models.PROTECT,null=True)
    def __str__(self):
        return self.name

#OneToOne
class Coupon(models.Model):
    code = models.TextField(max_length=40)
    relation = models.OneToOneField(User,on_delete=models.PROTECT)