from django.utils import timezone
from django.db import models


class Payment(models.Model):
    MONEY_TYPES = [
        ('credit', 'Credit'),
        ('debit', 'Debit'),
    ]
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('outcome', 'Outcome'),
    ]
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    money_type = models.CharField(max_length=6, choices=MONEY_TYPES, default='credit')
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES, default='income')
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.transaction_type} - {self.amount} {self.money_type}'
