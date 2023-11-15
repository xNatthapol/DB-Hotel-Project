from django.db import models


class Payment(models.Model):
    payment_datetime = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Account(models.Model):
    owner_name = models.CharField(max_length=255)
    income = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    outcome = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    transaction_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
