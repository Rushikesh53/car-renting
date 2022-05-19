from django.shortcuts import render
from django.views import View
from .models import Customer, Car, My_Order, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages

class CarView(View):
    def get(self, request):
        hatchback = Car.objects.filter(category='H')
        sedan = Car.objects.filter(category='S')
        suv = Car.objects.filter(category='SUV')
        muv = Car.objects.filter(category='MUV')
        return render(request, 'app/home.html',{'hatchback':hatchback, 'sedan':sedan, 'suv':suv, 'muv':muv})

class CarDetailView(View):
   def get(self, request, pk):
        car = Car.objects.get(pk=pk)
        return render(request,'app/cardetail.html',{'car':car})

def add_to_cart(request):
 user = request.user
 carid = request.GET.get('car_id')
 My_Order(user=user, car=carid).save()
 return render(request, 'app/addtocart.html')

def about_us(request):
 return render(request, 'app/aboutus.html')

def buy_now(request):
 return render(request, 'app/buynow.html')


def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def company(request, data=None):
 if data == None:
    cars = Car.objects.filter(category='H')
 elif data == 'Audi' or data == 'Toyota' or data == 'Hyundai' or data == 'Ford' or data == 'Honda' or data=="Tata" or data == 'Mercedes' or data == 'BMW' or data == 'Volvo' or data == 'KIA' :
    cars = Car.objects.filter(category='H').filter(brand=data)
 
 return render(request, 'app/company.html', {'cars':cars})

def companysedan(request, data=None):
 if data == None:
    cars = Car.objects.filter(category='S')
 elif data == 'Audi' or data == 'Toyota' or data == 'Hyundai' or data == 'Ford' or data == 'Honda' or data=="Tata" or data == 'Mercedes' or data == 'BMW' or data == 'Volvo' or data == 'KIA' :
    cars = Car.objects.filter(category='S').filter(brand=data)
 
 return render(request, 'app/companysedan.html', {'cars':cars})

def companysuv(request, data=None):
 if data == None:
    cars = Car.objects.filter(category='SUV')
 elif data == 'Audi' or data == 'Toyota' or data == 'Hyundai' or data == 'Ford' or data == 'Honda' or data=="Tata" or data == 'Mercedes' or data == 'BMW' or data == 'Volvo' or data == 'KIA' :
    cars = Car.objects.filter(category='SUV').filter(brand=data)
 
 return render(request, 'app/companysuv.html', {'cars':cars})

def companymuv(request, data=None):
 if data == None:
    cars = Car.objects.filter(category='MUV')
 elif data == 'Audi' or data == 'Toyota' or data == 'Hyundai' or data == 'Ford' or data == 'Honda' or data == 'Mercedes' or data == 'BMW' or data == 'Volvo' or data == 'KIA' :
    cars = Car.objects.filter(category='MUV').filter(brand=data)
 
 return render(request, 'app/companymuv.html', {'cars':cars})


class CustomerRegistrationView(View):
   def get(self, request):
      form = CustomerRegistrationForm()
      return render(request,'app/customerregistration.html',{'form':form})
   
   def post(self, request):
      form = CustomerRegistrationForm(request.POST)
      if form.is_valid():
         messages.success(request, 'Registration Successfull')
         form.save()
      return render(request,'app/customerregistration.html',{'form':form})

def checkout(request):
 return render(request, 'app/checkout.html')


class ProfileView(View):
   def get(self, request):
      form = CustomerProfileForm()
      return render(request, 'app/profile.html', {'form':form,'active':'btn-primary'})
   def post(self, request):
      form = CustomerProfileForm(request.POST)
      if form.is_valid():
         usr = request.user
         name = form.cleaned_data['name']
         locality = form.cleaned_data['locality']
         city = form.cleaned_data['city']
         state = form.cleaned_data['state']
         zipcode = form.cleaned_data['zipcode']
         mobile = form.cleaned_data['mobile']

         reg = Customer(user=usr, name=name, locality=locality, city=city , state=state, zipcode=zipcode, mobile=mobile)
         reg.save()
         messages.success(request, 'Profile Updated Successfully...!')
      return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})