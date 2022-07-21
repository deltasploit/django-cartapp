from django.db.models import Q

from .models import Customer
from products.models import Product, ProductCategory


def get_active_products(customer: Customer, category: ProductCategory=None):
    if category:
        return Product.objects.filter(Q(customer=customer), Q(active=True), Q(categories__name=category.name))
    return Product.objects.filter(Q(customer=customer), Q(active=True))


