from django.contrib import admin
from .models import Product, ProductCategory, ProductPrice



# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass


class ProductCategoryAdmin(admin.ModelAdmin):
    pass


class ProductPriceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(ProductPrice, ProductPriceAdmin)