from django.db import models

class Product(models.Model):
    print('Fields starts wirh _ are requried')
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=25)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=('images/%y/%m/%d'),blank=True) 
    descrption = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'phone'