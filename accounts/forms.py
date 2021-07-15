from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from address.forms import AddressField
from django.core.exceptions import ValidationError

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()


    class Meta:
        model= User
        fields= ["first_name",
                 "last_name",
                 "username",
                 "email",
                 "password1",
                 "password2"]

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email Already exists")
        elif User.objects.filter(username=username).exists():
            raise ValidationError("Username Already Taken")
        return self.cleaned_data

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['email']

class ProfileUpdateForm(forms.ModelForm):
    address = forms.CharField()
    mobile_number= forms.CharField()

    class Meta:
        model = Profile
        fields =['image','address','mobile_number']
