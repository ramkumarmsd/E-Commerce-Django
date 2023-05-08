from django.db import models
from django.contrib.auth.models import User
import datetime
import os

# Create your models here.

def getfile(request,filename):
    ctime=datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")
    new_filename="%s%s"%(ctime,filename)
    return os.path.join('uploads',new_filename) 

class category(models.Model):
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=getfile,null=True,blank=True)
    description=models.TextField(max_length=300,null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0-show ,1-hidden')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class product(models.Model):
    catagory=models.ForeignKey(category,on_delete=models.CASCADE)
    name = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=getfile,null=True,blank=True)
    description=models.TextField(max_length=300,null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    original_price = models.IntegerField(null=False,blank=False)
    selling_price = models.IntegerField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text='0-show ,1-hidden')
    trending = models.BooleanField(default=False,help_text='0-default ,1-trending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    product_qtn = models.IntegerField(null=False,blank=False)    
    created_at=models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qtn*self.products.selling_price

class favourite(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ForeignKey(product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)