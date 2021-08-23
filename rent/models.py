from django.db import models
import sys

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 40)
	email = models.EmailField()
	phone_number = models.CharField(max_length = 20) # from phonenumber_field.modelfields import PhoneNumberField
	address = models.CharField(max_length = 100)
	city = models.CharField(max_length = 30)
	country = models.CharField(max_length = 30)

	def __repr__(self):
		return f'{self.first_name}, {self.last_name}'

	def __str__(self):
		return f'{self.first_name}, {self.last_name}' 


class VehicleType(models.Model):
	name = models.CharField(max_length = 30)

	def __str__(self):
		return f'{self.name}' 

class VehicleSize(models.Model):
	name = models.CharField(max_length = 15) 

	def __str__(self):
		return f'{self.name}'

class Vehicle(models.Model):
	vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
	date_created = models.DateField(null=True, blank=True)
	real_cost =  models.FloatField(default=0)
	size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)


	def __repr__(self):
		return f"{self.vehicle_type}, {self.size}"

	def __str__(self):
		return f"{self.vehicle_type}, {self.size}"

class Rental(models.Model):
	rental_date = models.DateTimeField()
	return_date = models.DateTimeField()
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

	def __repr__(self):
		return f'{self.customer}, {self.vehicle}'

	def __str__(self):
		return f'{self.customer}, {self.vehicle}'



class RentalRate(models.Model):
	daily_rate = models.FloatField(default=0)
	vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE) 
	vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE) 

	def __str__(self):
		return f'{self.vehicle_type}, {self.vehicle_size}'






