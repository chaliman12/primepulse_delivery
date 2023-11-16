# primepulse_delivery/core/models.py

from django.db import models

class Order(models.Model):
    order_number = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    # Add more fields as needed (e.g., delivery_address, items, status, etc.)

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=15)
    capacity = models.IntegerField()
    # Add more fields as needed

# Add more models as required
