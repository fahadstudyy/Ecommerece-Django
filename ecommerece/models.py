from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model

class product(models.Model):
    name = models.CharField(max_length=50)
    date_create = models.DateTimeField(auto_now_add=True)
    descreption = models.TextField(max_length=1000)
    qty = models.IntegerField(default=0)
    Image = models.ImageField(upload_to = 'myshop/produtc-images/', null=True, blank =True )
    URL = models.URLField(blank= True)
    price = models.IntegerField(default=0)
    

    def __str__(self):
        return self.name

    

    @property
    def imageURL(self):
        try: 
            url = self.Image.url
        except:
            url = ''
        return url

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True )
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null= True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null = True, blank= False)
    transaction_id= models.CharField(max_length=100, null=True) 

    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quanity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(product,on_delete=models.SET_NULL, null=True)   
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
    quanity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)   

    @property
    def get_total(self):
        total = self.quanity * self.product.price
        return total

class ShippingAddress(models.Model):
     customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True)
     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
     address = models.CharField(max_length=200, null=False)
     city = models.CharField(max_length=200, null=False)
     state = models.CharField(max_length=200, null=False)
     zip = models.CharField(max_length=200, null=False)
     date_added = models.DateTimeField(auto_now_add=True)
     
     
     def __str__(self):
        return self.address
