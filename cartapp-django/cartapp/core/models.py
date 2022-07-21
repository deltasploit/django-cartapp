from datetime import datetime

from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)
    #TODO add photo

    def __str__(self) -> str:
        return self.name


class CustomerConfig(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    max_products = models.IntegerField(100)
    #theme = models.OneToOneField(Theme)

    def __str__(self) -> str:
        return f'{self.customer.name} config'