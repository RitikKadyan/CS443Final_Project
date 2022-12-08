from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("index/", views.index, name="index"),

    path("customer/", views.customer, name="customer"),
    path("customer/create/", views.cus_create, name="cus_create"),
    path("customer/read/", views.cus_read, name="cus_read"),
    path("customer/edit/", views.cus_edit, name="cus_edit"),
    path("customer/delete/", views.cus_delete, name="cus_delete"),

    path("employee/", views.employee, name="employee"),
    path("employee/create/", views.emp_create, name="emp_create"),
    path("employee/read/", views.emp_read, name="emp_read"),
    path("employee/edit/", views.emp_edit, name="emp_edit"),
    path("employee/delete/", views.emp_delete, name="emp_delete"),

    path("games/", views.games, name="games"),
    path("transactions/", views.transaction, name="transactions"),

    path("cus/", views.cus_view, name="cus_view"),
    path("cus/buy/", views.cus_buy, name="cus_buy"),
    path("cus/orders/", views.cus_order, name="cus_order"),

    path("register/", views.register, name="register"),



]
