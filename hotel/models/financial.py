from django.db import models


class Account(models.Model):
    id_account = models.CharField(primary_key=True, max_length=10)
    owner_name = models.CharField(max_length=255)
    income = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    outcome = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)


class Payment(models.Model):
    transaction_id = models.CharField(primary_key=True, max_length=10)
    payment_datetime = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payer = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='payments_made')
    receiver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='payments_received')

