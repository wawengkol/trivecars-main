from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("",views.home, name="home"),
    path("home",views.home, name="home"),
    path("vehicles/<str:category>/",views.vehicles, name="vehicles"),
    path("create_rent/<str:pk>/", views.create_rent, name='create_rent'),
    path("rent_details",views.rent_details,name='rent_details'),
    path("rented_successfully",views.rented_successfully,name='rented_successfully'),
    path("admin_dash",views.admin_dash,name='admin_dash'),
    path("add_cars",views.add_cars,name='add_cars'),
    path("add_staff",views.add_staff,name='add_staff'),
    path("delete_item/<str:item>/<str:pk>/",views.delete_item,name='delete_item'),
    path("edit_cars/<str:pk>/",views.edit_cars,name='edit_cars'),
    path("edit_rent/<str:pk>/",views.edit_rent,name='edit_rent'),
]
