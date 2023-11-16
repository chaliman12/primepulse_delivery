# primepulse_delivery/core/views.py

from rest_framework import generics
from .models import Order, Vehicle
from .serializers import OrderSerializer, VehicleSerializer

# primepulse_delivery/core/views.py

from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'home.html')

def order_form(request):
    return render(request, 'order_form.html')

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class VehicleListCreateView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
