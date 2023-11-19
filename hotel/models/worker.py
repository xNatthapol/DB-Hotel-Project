from django.db import models
from django.utils import timezone


class Role(models.Model):
    role_name = models.CharField(max_length=100)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)


class Employee(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    hire_date = models.DateField(default=timezone.now)
