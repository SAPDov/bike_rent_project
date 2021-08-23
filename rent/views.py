from django.shortcuts import HttpResponse, render, redirect, get_object_or_404, get_list_or_404
from .models import Customer, VehicleType, VehicleSize, Vehicle, Rental, RentalRate
from .forms import AddRentalForm, AddCustomerForm, AddVehicleForm

# Create your views here.

def home(request):
	return render(request, 'homepage.html')


def rental(request):
	r = Rental.objects.order_by('return_date').all()
	return render(request, 'rental.html',{'rentals': r})

def rental_id(request, id):
	rental = Rental.objects.filter(id=id)
	customer = Customer.objects.filter(rental__id=id)
	vehicle = Vehicle.objects.filter(rental__id=id)
	vehicle_index = Vehicle.objects.get(rental__id=id)

	# print(vehicle_index)
	# print(vehicle) add the size and type of vehicle
	context = {'rental': rental,
				'customer': customer,
				'vehicle': vehicle}

	return render(request, 'rental_id.html', context)
	
def add_rental(request):
	if request.method == 'GET':
		form = AddRentalForm()
	
	if request.method == 'POST':
		form = AddRentalForm(request.POST)

		if form.is_valid():
			customer_id = form.cleaned_data['customer_id'] 		
			vehicle_id = form.cleaned_data['vehicle_id']
			rental_date = form.cleaned_data['rental_date']
			return_date = form.cleaned_data['return_date']
			rf = Rental(customer_id=customer_id, vehicle_id=vehicle_id, rental_date=rental_date, return_date=return_date)
			rf.save()
			return redirect('rental')
	else:
		return render(request, 'add_rental.html', {'form':form})
	
	
def customer(request):
	c = Customer.objects.order_by('last_name').all()
	return render(request, 'customer.html' , {'customer': c})


def customer_id(request, id):
	c = Customer.objects.filter(id=id)
	return render(request, 'customer_id.html', {'customer':c})


def add_customer(request):
	if request.method == 'GET':
		form = AddCustomerForm()
	if request.method == 'POST':
		form = AddCustomerForm(request.POST)

		if form.is_valid():
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']
			email = form.cleaned_data['email']
			phone_number = form.cleaned_data['phone_number'] 
			address = form.cleaned_data['address'] 
			city = form.cleaned_data['city'] 
			country = form.cleaned_data['country'] 

			cf=Customer(first_name=first_name,
						last_name=last_name,
						email=email,
						phone_number=phone_number,
						address=address,
						city=city,
						country=country)
			cf.save()
			return redirect('customer')
	else:
		return render(request, 'customer_add.html', {'form':form})


def vehicle(request):
	v = Vehicle.objects.all()
	return render (request, 'vehicle.html', {'vehicle': v} )

def vehicle_id(request, id):
	v = Vehicle.objects.filter(id=id)
	r = Rental.objects.filter(vehicle__id=id)
	context = {'vehicle': v,
				'rental': r}
	return render (request, 'vehicle_id.html', context)

def vehicle_add(request):
	if request.method == 'GET':
		form = AddVehicleForm()
	if request.method == 'POST':
		form = AddVehicleForm(request.POST)

		if form.is_valid():
			vehicle_type = form.cleaned_data['vehicle_type']
			date_created = form.cleaned_data['date_created']
			real_cost = form.cleaned_data['real_cost']
			size = form.cleaned_data['size'] 
		 

			vf=Vehicle(vehicle_type=vehicle_type,
						date_created=date_created,
						real_cost=real_cost,
						size=size)
			vf.save()
			return redirect('vehicle')
	else:
		return render(request, 'vehicle_add.html', {'form':form})












	







