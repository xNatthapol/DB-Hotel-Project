from django.db import models


class Customer(models.Model):
    phone_number = models.CharField(max_length=10)
    fname = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()
