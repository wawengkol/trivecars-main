from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from RENTaCAR.models import Car_order
from .forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from address.models import Address
from django.conf import settings

# Create your views here.
def login(request):
    return render(request,"Login.html")

@login_required
def profile(request):
    user=request.user
    details=Car_order.objects.filter(user_id=user.id)
    if request.method == 'POST':

        u_form=UserUpdateForm(request.POST, instance=user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        currentPassword=request.POST.get('currentPassword',False)
        password1=request.POST.get('newpass',False)
        password2=request.POST.get('checkpass',False)

        if password1==password2 and user.check_password(currentPassword):
            user.set_password(password1)
            user.save()
            update_session_auth_hash(request,user)

        elif u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:

        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile)
    context = {
        'details':details,
        'u_form':u_form,
        'p_form':p_form
    }
    print(details)
    return render(request,"profile.html",context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f"You're Ready to Login")
            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request,"register.html",{'form':form})
