from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Car_order,Cars

class DateInput(forms.DateInput):
    input_type = 'date'

class RentForm(forms.ModelForm):
    duration=forms.IntegerField()
    delivery_address= forms.CharField()

    class Meta:
        model=Car_order
        fields='__all__'
        widgets = {
            'expected_delivery':DateInput()
        }

class CarsForm(forms.ModelForm):
    class Meta:
        model=Cars
        fields='__all__'

class UpdateCarForm(forms.ModelForm):
    class Meta:
        model=Cars
        fields=['car_type','brand','model','price']

class UpdateRentForm(forms.ModelForm):
    class Meta:
        model=Car_order
        fields=['user','car_model','duration','delivery_address','status']

class AddStaffForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name",
                 "last_name",
                 "username",
                 "email",
                 "password1",
                 "password2",
                 "is_staff"]
