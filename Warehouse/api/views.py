from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from api.serializers import AddressSerializer, EmployeeSerializer, InvoiceSerializer, ProductSerializer, CallendarSerializer
from .models import Employee, Invoice, Product, Callendar


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    
    def get_serializer_context(self):
        return {'request':self.request}


class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    
    def get_serializer_context(self):
        return {'request':self.request}


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_context(self):
        return {'request':self.request}


class CallendarViewSet(ModelViewSet):
    queryset = Callendar.objects.all()
    serializer_class = CallendarSerializer
    
    def get_serializer_context(self):
        return {'request':self.request}

