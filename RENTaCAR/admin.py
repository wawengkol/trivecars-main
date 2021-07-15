from django.contrib import admin
from .models import Car_order, Cars, CarType

# Register your models here.
admin.site.register(Car_order)
admin.site.register(Cars)
admin.site.register(CarType)
