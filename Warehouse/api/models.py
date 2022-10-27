from email.policy import default
from django.db import models
from address.models import AddressField
from phone_field import PhoneField
from django.core.validators import MinValueValidator


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField()
    phone = PhoneField(blank=True, null=True)
    address = AddressField(related_name='+', blank=True, null=True)
    working_time = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name']


class Invoice(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['completed']


class Collection(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    inventory = models.IntegerField(validators=[MinValueValidator(0)])
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products')

    def __str__(self) -> str:
        return self.title


class Callendar(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return self.title


