from django.db import models

class Product(models.Model):
    category_list = [('phone','phone'),
                     ('computer','computer'),
                     ('monitor','monitor'),
                     ('accessories','accessories'),
                    ]
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=25,choices=category_list)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(
                                upload_to='images/%y/%m/%d',
                                blank=True,
                                null=True
                            )
    description  = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'phone'