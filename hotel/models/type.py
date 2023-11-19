from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=255)
    cost_per_hour = models.IntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    floor = models.IntegerField()
    room_type = models.CharField(max_length=255)
    accommodates = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        return f"{self.room_type} - Floor {self.floor} - Accommodates {self.accommodates} - {availability}"