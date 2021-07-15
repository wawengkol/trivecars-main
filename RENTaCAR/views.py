from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Car_order, Cars,CarType
from django.contrib.auth.models import User
from .forms import RentForm,CarsForm,UpdateCarForm,UpdateRentForm,AddStaffForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

import datetime




# Create your views here.

def home(request):
    return render(request,"home.html")

def vehicles(request,category):
    cars=Cars.objects.all()
    if category!='all':
        cars=Cars.objects.filter(car_type_id=category)
    paginator = Paginator(cars, 6)
    page = request.GET.get('page')
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)
    context ={
        'cars': cars,
        }
    return render(request,"Vehicles.html",context)

@login_required
def create_rent(request, pk):
    car=Cars.objects.get(id=pk)
    if request.method == 'POST':
        form = RentForm(request.POST,initial={'car_model':car.model,'sub_total':car.price,'user':request.user})
        if form.is_valid():
            print("here?")
            form.save()
            return redirect('rented_successfully')

    form=RentForm(initial={'car_model':car.model,'sub_total':car.price,'user':request.user})

    context = {
        "car":car,
        "form": form,
    }
    return render(request, 'create_rent.html', context)

@login_required
def rented_successfully(request):
    return render(request,'rented_successfully.html')

@login_required
def rent_details(request):
    details=Car_order.objects.latest()
    total=int(details.duration)*int(details.sub_total)
    details.amount_payable=total
    new_total=Car_order.objects.filter(pk=details.pk).update(amount_payable=total)
    context={
        'details':details,
        'total':total
    }
    return render(request,'rent_details.html',context)

@login_required
def admin_dash(request):
    member=request.user
    if member.is_staff:
        day_sales=[0]
        month_sales=[0]
        year_sales=[0]
        users=User.objects.order_by("date_joined")
        cars=Cars.objects.order_by("id")
        car_orders=Car_order.objects.order_by("order_date")
        now=datetime.datetime.now()
        all_orders=Car_order.objects.all()
        for item in all_orders:
            if item.order_date.date()==now.date():
                day_sales.append(item.amount_payable)
                month_sales.append(item.amount_payable)
                year_sales.append(item.amount_payable)
            elif item.order_date.month==now.month and item.order_date.year==now.year:
                month_sales.append(item.amount_payable)
                year_sales.append(item.amount_payable)
            elif item.order_date.year==now.year:
                year_sales.append(item.amount_payable)

        total_items={
            'day_sales':sum(day_sales),
            'month_sales':sum(month_sales),
            'year_sales':sum(year_sales),
            'users':len(users),
            'cars':len(cars),
            'car_orders':len(car_orders)
        }
        context={
            'total_items':total_items,
            'users':users,
            'cars':cars,
            'car_orders':car_orders
        }
        return render(request,'admin_dash.html',context)

    else:
        raise PermissionDenied




@login_required
def add_cars(request):
    member=request.user
    if member.is_staff:
        if request.method=='POST':
            form=CarsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('admin_dash')
        form=CarsForm()
        return render(request,'add_item.html',{'form':form})
    else:
        raise PermissionDenied

@login_required
def add_staff(request):
    member=request.user
    if member.is_staff:
        if request.method=='POST':
            form=AddStaffForm(request.POST,initial={'is_staff':True})
            if form.is_valid():
                form.save()
                return redirect('admin_dash')
        form=AddStaffForm(initial={'is_staff':True})
        context={
            'form':form,
        }
        return render(request,'add_item.html',context)

    else:
        raise PermissionDenied


@login_required
def edit_cars(request,pk):
    member=request.user
    if member.is_staff:
        car=Cars.objects.get(id=pk)
        if request.method=='POST':
            form=UpdateCarForm(request.POST,instance=car)
            if form.is_valid():
                form.save()
                return redirect('admin_dash')

        form=UpdateCarForm(instance=car)
        return render(request,'editTemp.html',{'form':form})

    else:
        raise PermissionDenied

@login_required
def edit_rent(request,pk):
    member=request.user
    if member.is_staff:
        carRent=Car_order.objects.get(id=pk)
        if request.method=='POST':
            form=UpdateRentForm(request.POST,instance=carRent)
            if form.is_valid():
                form.save()
                return redirect('admin_dash')

        form=UpdateRentForm(instance=carRent)
        return render(request,'editTemp.html',{'form':form})

    else:
        raise PermissionDenied

@login_required
def delete_item(request,item,pk):
    user=request.user
    if user.is_staff:
        if item=='user':
            delete=User.objects.get(id=pk)
            if request.method=='POST':
                delete.delete()
                update_session_auth_hash(request,user)
                return redirect('admin_dash')
        elif item=='cars':
            delete=Cars.objects.get(id=pk)
            if request.method=='POST':
                delete.delete()
                return redirect('admin_dash')
        elif item=='order':
            delete=Car_order.objects.get(id=pk)
            if request.method=='POST':
                delete.delete()
                return redirect('admin_dash')
        return render(request,'delete_item.html')

    else:
        raise PermissionDenied
