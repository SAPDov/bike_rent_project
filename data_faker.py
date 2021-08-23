from faker import Faker
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()
from rent.models import Customer, VehicleType, VehicleSize, Vehicle, Rental, RentalRate

def create_customer_rental():
	fake = Faker()
	



	Customer.objects.create(first_name = fake.first_name(),
							last_name = fake.last_name(),
							email = fake.ascii_free_email(),
							phone_number = fake.phone_number(),
							address = fake.street_address(),
							city = fake.city(),
							country = fake.country())
	
	

	Rental.objects.create(rental_date = fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None),
	# 						return_date = fake.date_time_this_decade(before_now=False, after_now=True, tzinfo=None))





		
# for i in range(15):
# 	create_customer_rental()

