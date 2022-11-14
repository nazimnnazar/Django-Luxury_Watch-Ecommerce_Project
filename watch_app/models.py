# from django.db import models
# from django.urls import reverse

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse



# Create your models here.
class Categ(models.Model):
    name= models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250,unique=True)

    class meta:
        ordering=('name,')
        verbose_name='category'
        verbose_name = plural ='categories'

    def get_url(self):
        return reverse('product', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=230,unique=True)
    img = models.ImageField(upload_to='products')
    desc = models.TextField()
    stock = models.IntegerField()
    available = models.BooleanField()
    price = models.IntegerField()
    category = models.ForeignKey(Categ,on_delete=models.CASCADE)
    

    def get_url(self):
        return reverse('productviews',args=[self.category.slug,self.slug])

    def __str__(self):
        return '{}'.format(self.name) 

#cart

class CartList(models.Model):
    cart_id = models.CharField(max_length=200, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItems(models.Model):
    prod = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList, on_delete=models.CASCADE)
    quan = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.prodt

    def total(self):
        return self.prod.price * self.quan
#end cart