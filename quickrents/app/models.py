from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICE = (
    ('Maharashtra','Maharashtra'),
    ('Rajasthan','Rajasthan'),
    ('Delhi','Delhi'),
    ('Tamil Nadu','Tamil Nadu'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Gujrat','Gujrat'),
)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=50)
    mobile = models.IntegerField()

    def __str__(self):
        return str(self.id)




CATEGORY_CHOICES = (
    ('H','HATCHBACK'),
    ('S','SEDAN'),
    ('SUV','SUV'),
    ('MUV','MUV'),
)

class Car(models.Model):
    title = models.CharField(max_length=100)
    renting_price = models.FloatField()
    description = models.TextField()
    mileage=models.CharField(max_length=2)
    brand = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    car_image = models.ImageField(upload_to='carimg')

    def __str__(self):
        return str(self.id)

class My_Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.id)
    
STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    def __str__(self):
        return str(self.id)