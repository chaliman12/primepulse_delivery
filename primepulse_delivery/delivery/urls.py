# primepulse_delivery/core/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('order/', order_form, name='order-form'),
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('vehicles/', VehicleListCreateView.as_view(), name='vehicle-list-create'),
    # Add more URLs as needed
]
