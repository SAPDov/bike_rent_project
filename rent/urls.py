from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
	path('home', views.home, name='home'),
    path('rental', views.rental, name='rental'),
    path('rental_id/<int:id>', views.rental_id, name='rental_id'),
    path('add_rental', views.add_rental, name='add_rental'),
    path('customer', views.customer, name='customer'),
    path('customer_id/<int:id>', views.customer_id, name='customer_id'),
    path('add_customer', views.add_customer, name='add_customer'),
    path('vehicle', views.vehicle, name='vehicle'),
    path('vehicle_id/<int:id>', views.vehicle_id, name='vehicle_id'),
    path('vehicle_add', views.vehicle_add, name='vehicle_add'),
]
