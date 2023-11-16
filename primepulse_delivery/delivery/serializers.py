# primepulse_delivery/core/serializers.py

from rest_framework import serializers
from .models import Order, Vehicle

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
