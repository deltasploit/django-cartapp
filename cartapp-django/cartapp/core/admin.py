from django.contrib import admin

from .models import Customer, CustomerConfig


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    pass


class CustomerConfigAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerConfig, CustomerConfigAdmin)