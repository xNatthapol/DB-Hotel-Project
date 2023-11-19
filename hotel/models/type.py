from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=100)
    cost_per_hour = models.IntegerField()

    def __str__(self):
        return self.name

class Room(models.Model):
    FLOOR_CHOICES = [(i, f"Floor {i}") for i in range(1, 11)]
    ROOM_TYPE_CHOICES = [
        ('Single', 'Single'),
        ('Double', 'Double'),
        ('Suite', 'Suite'),
        ('Penthouse', 'Penthouse'),
    ]

    floor = models.IntegerField(choices=FLOOR_CHOICES)
    room_type = models.CharField(max_length=30, choices=ROOM_TYPE_CHOICES)
    accommodates = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        availability = "Available" if self.is_available else "Not Available"
        return f"{self.room_type} - Floor {self.floor} - Accommodates {self.accommodates} - {availability}"
