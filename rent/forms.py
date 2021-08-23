from django import forms
from .models import Rental


class AddRentalForm(forms.Form):
    customer_id = forms.IntegerField(required=True, 
    								label="Customer-id",
    								error_messages={'required': 'Please enter a valid customer_id'})
    vehicle_id = forms.IntegerField(required=True,
    								label="Vehicle-id",
    							  	error_messages={'required': 'Please enter a valid vehicle_id'})

    rental_date = forms.DateTimeField(label='Rental Date')
    return_date = forms.DateTimeField(required = False, label= 'Return Date')


class AddCustomerForm(forms.Form):
	first_name = forms.CharField(max_length = 30)
	last_name = forms.CharField(max_length = 40)
	email = forms.EmailField()
	phone_number = forms.CharField(max_length = 20) 
	address = forms.CharField(max_length = 100)
	city = forms.CharField(max_length = 30)
	country = forms.CharField(max_length = 30)


class AddVehicleForm(forms.Form):
	vehicle_type = forms.IntegerField()
	size = forms.IntegerField()
	real_cost = forms.FloatField()
	date_created = forms.DateField()




