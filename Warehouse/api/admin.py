from ast import Call
from django.contrib import admin
from .models import Employee, Invoice, Product, Collection, Callendar

admin.site.register(Employee)
admin.site.register(Invoice)
admin.site.register(Product)
admin.site.register(Collection)
admin.site.register(Callendar)

