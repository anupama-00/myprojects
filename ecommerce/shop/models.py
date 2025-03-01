from django.db import models
from django.db.models import Model


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    image=models.ImageField(upload_to="media/images")

    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=40)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to="media/products",blank=True,null=True)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="product")

    def __str__(self):
        return self.name

