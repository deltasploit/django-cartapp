from django.db.models import Q

from .models import Product, ProductPrice


def get_current_price(product: Product):
    """ Returns ProductPrice object for product """
    return ProductPrice.objects.get(Q(active=True), Q(product=product))


def set_price(product: Product, price):
    old_price = get_current_price(product)
    old_price.active = False
    old_price.save()
    new_price = ProductPrice(product=product, price=price, active=True)
    new_price.save()