from django.db import models
from django.utils import timezone


class Role(models.Model):
    role_name = models.CharField(max_length=100)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)


class Employee(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    hire_date = models.DateField(default=timezone.now)
