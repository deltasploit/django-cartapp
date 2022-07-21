from rest_framework import serializers
from .models import Customer, CustomerConfig


class CustomerSerializer(serializers.ModelSerializer):
    max_products = serializers.SlugRelatedField(
        many=False,
        slug_field='max_products',
        read_only=True
    )

    class Meta:
        model = Customer
        fields = ['name', 'description', 'created_at', 'max_products']