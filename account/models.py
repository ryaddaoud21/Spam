from django.db import models


class Customers(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
      return  self.name

class Tag (models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
      return  self.name
class Product (models.Model):
    categori = (
        ('indore', 'indore'),
        ('outdore', 'outdore'),
    )
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category= models.CharField(max_length=200, null=True , choices= categori)
    description= models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):

    status = (
        ('pending', 'pending'),
        ('out of delivry','out of delivry'),
        ('delivred','delivred'),
    )
    customers = models.ForeignKey(Customers , null=True , on_delete= models.SET_NULL)
    products = models.ForeignKey(Product , null=True , on_delete= models.SET_NULL)
    cas = models.CharField(max_length=200, null=True , choices= status)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.customers.name