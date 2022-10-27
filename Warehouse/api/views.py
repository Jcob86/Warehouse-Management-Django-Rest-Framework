from django.shortcuts import render
from django.db.models.aggregates import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from api.serializers import AddressSerializer, EmployeeSerializer, InvoiceSerializer,CollectionSerializer, ProductSerializer, CallendarSerializer
from .models import Employee, Invoice, Product, Callendar, Collection


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['last_name']
    ordering_fields = ['last_name']
    
    def get_serializer_context(self):
        return {'request':self.request}


class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [IsAdminUser]
    
    def get_serializer_context(self):
        return {'request':self.request}


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def get_serializer_context(self):
        return {'request':self.request}


class CallendarViewSet(ModelViewSet):
    queryset = Callendar.objects.all()
    serializer_class = CallendarSerializer
    permission_classes = [IsAdminUser]
    
    def get_serializer_context(self):
        return {'request':self.request}

