from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("customer/", views.customer, name="customer"),
    path("customer/create/", views.cus_create, name="cus_create"),
    path("customer/read/", views.cus_read, name="cus_read"),
    path("customer/edit/", views.cus_edit, name="cus_edit"),
    path("customer/delete/", views.cus_delete, name="cus_delete"),
]
