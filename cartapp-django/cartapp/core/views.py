from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from rest_framework import viewsets

from .serializers import CustomerSerializer
from .models import Customer, CustomerConfig



# Create your views here.
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'


class CustomerConfigListView(ListView):
    model = CustomerConfig


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['name', 'description']
    template_name = 'customer_create.html'
    success_url = reverse_lazy('customer-list')


class CustomerConfigCreateView(CreateView):
    model = CustomerConfig


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
