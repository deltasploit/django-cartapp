from datetime import datetime
from django.db import models

from core.models import Customer


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    categories = models.ManyToManyField(ProductCategory)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self) -> str:
        return self.name

    def is_active(self):
        return self.active


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()
    created_at = models.DateTimeField(default=datetime.now)
    active = models.BooleanField()
