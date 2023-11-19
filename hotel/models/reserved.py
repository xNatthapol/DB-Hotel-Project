from django.db import models


class ReservedRoom(models.Model):
    customer = models.ForeignKey('hotel.Customer', on_delete=models.CASCADE)
    room = models.ForeignKey('hotel.Room', on_delete=models.CASCADE)
    room_number = models.IntegerField()
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()


class ReservedFacility(models.Model):
    customer = models.ForeignKey('hotel.Customer', on_delete=models.CASCADE)
    facility = models.ForeignKey('hotel.Facility', on_delete=models.CASCADE)
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField()
