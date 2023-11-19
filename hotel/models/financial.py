from django.utils import timezone
from django.db import models


class Payment(models.Model):
    TRANSACTION_TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    description = models.TextField()
    timestamp = models.DateTimeField(deafult=timezone.now)


class Account(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('outcome', 'Outcome'),
    ]
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
