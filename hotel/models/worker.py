from django.db import models


class Employee(models.Model):
    class Meta:
        abstract = True


class HeadChef(Employee):
    pass


class Accountant(Employee):
    pass
