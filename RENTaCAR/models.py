from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class CarType(models.Model):
    type = models.CharField(max_length = 50)

    def __str__(self):
        return self.type

class Cars(models.Model):
    car_type = models.ForeignKey(CarType, on_delete = models.CASCADE, null = True)
    brand = models. CharField(max_length=50)
    image=models.ImageField(upload_to='car_pics')
    model= models.CharField(max_length=100)
    specifications = models.TextField(max_length=4000)
    price=models.IntegerField(help_text="Per Day")

    class Meta:
        verbose_name_plural = "Cars"

    def __str__(self):
        return f"{self.car_type} {self.model}"

class Car_order(models.Model):
    STATUS=(
        ("On Process","On Process"),
        ("Delivered","Delivered"),
        ("Returned","Returned")
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    car_model = models.CharField(max_length=100, null=True)
    sub_total= models.IntegerField()
    order_date=models.DateTimeField(auto_now_add=True, blank=True)
    expected_delivery=models.DateTimeField(null=True)
    duration=models.IntegerField()
    delivery_address= models.CharField(max_length=100)
    status=models.CharField(max_length=20,null=True,default=STATUS[0][0], choices=STATUS)
    amount_payable=models.IntegerField(null=True,blank=True)

    class Meta:
        get_latest_by='order_date'

    def __str__(self):
         return f'{self.user} Order'







# Create your models here.
