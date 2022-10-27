from decimal import Decimal
from rest_framework import serializers
from . import models
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['formatted']


class EmployeeSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    class Meta:
        model = models.Employee
        fields = ['id','first_name', 'last_name', 'birth_date', 'email', 'phone', 'working_time', 'position', 'address']


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = '__all__'


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer()
    class Meta:
        model = models.Product
        fields = ['id', 'title', 'price','price_with_tax', 'description', 'inventory', 'collection']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product:models.Product):
        return product.price*Decimal(1.1)


class CallendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Callendar
        fields = '__all__'

