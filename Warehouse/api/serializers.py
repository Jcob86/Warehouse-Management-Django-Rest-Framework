from rest_framework import serializers
from . import models
from address.models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['formatted']


class EmployeeSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
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
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer()
    class Meta:
        model = models.Product
        fields = ['id', 'title', 'price', 'description', 'inventory', 'collection']


class CallendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Callendar
        fields = '__all__'

