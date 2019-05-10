from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=30)
    photo=models.ImageField(upload_to='static/images/products/')
    description=models.CharField(max_length=200)
    category=models.ForeignKey(Category, on_delete=models.CASCADE )
    purchase_price=models.IntegerField()
    sale_price=models.IntegerField()

    def __str__(self):
        return self.name
class Purchase(models.Model):
    buyer=models.ForeignKey(User , on_delete=models.CASCADE )
    pruduct=models.ManyToManyField(Product )
    status=models.CharField(max_length=1, default='w', choices=(('w', 'waiting for payment'), ('s', 'shiping'), ('c', 'completed')))

class Phone(models.Model):
    phone=models.CharField(max_length=11)
    user=models.ForeignKey(User, on_delete=models.CASCADE )

class Shipping_Address(models.Model):
    buyer=models.ForeignKey(User, on_delete=models.CASCADE)
    state=models.CharField(max_length=20)
    township=models.CharField(max_length=30)
    bus_gate=models.CharField(max_length=100)
