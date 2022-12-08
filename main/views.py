from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

# Links to all pages
def index(response):
    return render(response, "main/index.html", {})


# Customer Page
def customer(response):
    return render(response, "main/customer.html", {})


# Customer create page
def cus_create(response):
    if response.method == "POST":
        form = CustomerCreateForm(response.POST)

        if form.is_valid():

            f_name = form.cleaned_data["f_name"]
            l_name = form.cleaned_data["l_name"]
            age = form.cleaned_data["age"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = User.objects.create_user(first_name=f_name, last_name=l_name, username=username, password=password)
            user.save()
            c = Customer(f_name=f_name, l_name=l_name, age=age, username=username, password=password)
            c.save()
        # Redirects to customer/read
        return HttpResponseRedirect("../read")
    else:
        form = CustomerCreateForm()
    return render(response, "main/cus_create.html", {"form": form})


# Customer Read Page
def cus_read(response):
    cus = Customer.objects  # Get all customers
    data = []
    for c in cus.all():
        data.append(c)
    return render(response, "main/cus_read.html", {"cus": cus, "data": data})  # Render page and pass customers


# Customer Read Page
def cus_edit(response):
    if response.method == "POST":
        form = CustomerEditForm(response.POST)

        if form.is_valid():
            id_ = form.cleaned_data["id"]
            f_name = form.cleaned_data["f_name"]
            l_name = form.cleaned_data["l_name"]
            age = form.cleaned_data["age"]
            c = Customer.objects.get(id=id_)
            c.f_name = f_name
            c.l_name = l_name
            c.age = age
            c.save()
        # Redirects to customer/read
        return HttpResponseRedirect("../read")
    else:
        form = CustomerEditForm()
    return render(response, "main/cus_edit.html", {"form": form})


# Customer Delete Page
def cus_delete(response):
    if response.method == "POST":
        form = CustomerDeleteForm(response.POST)

        try:
            if form.is_valid():
                id_ = form.cleaned_data["id"]
                c = Customer.objects.get(id=id_)
                c.delete()
            # Redirects to customer/read
            return HttpResponseRedirect("../read")
        except ObjectDoesNotExist:
            return HttpResponseRedirect("../")
    else:
        form = CustomerDeleteForm()
        return render(response, "main/cus_delete.html", {"form": form})


def employee(response):
    return render(response, "main/employee.html", {})


def emp_create(response):
    if response.method == "POST":
        form = EmployeeCreateForm(response.POST)

        if form.is_valid():
            emp_first_name = form.cleaned_data["emp_first_name"]
            emp_last_name = form.cleaned_data["emp_last_name"]
            emp_pay = form.cleaned_data["emp_pay"]
            c = Employee(emp_first_name=emp_first_name, emp_last_name=emp_last_name, emp_pay=emp_pay)
            c.save()
        # Redirects to customer/read
        return HttpResponseRedirect("../read")
    else:
        form = EmployeeCreateForm()
    return render(response, "main/emp_create.html", {"form": form})


def emp_read(response):
    emp = Employee.objects  # Get all employees
    data = []
    for e in emp.all():
        data.append(e)
    return render(response, "main/emp_read.html", {"emp": emp, "data": data})  # Render page and pass customers


def emp_edit(response):
    if response.method == "POST":
        form = EmployeeEditForm(response.POST)

        if form.is_valid():
            id_ = form.cleaned_data["id"]
            emp_first_name = form.cleaned_data["emp_first_name"]
            emp_last_name = form.cleaned_data["emp_last_name"]
            emp_pay = form.cleaned_data["emp_pay"]

            e = Employee.objects.get(id=id_)
            e.emp_first_name = emp_first_name
            e.emp_last_name = emp_last_name
            e.emp_pay = emp_pay
            e.save()
        # Redirects to Employee/read
        return HttpResponseRedirect("../read")
    else:
        form = EmployeeEditForm()
    return render(response, "main/emp_edit.html", {"form": form})


def emp_delete(response):
    if response.method == "POST":
        form = EmployeeDeleteForm(response.POST)

        try:
            if form.is_valid():
                id_ = form.cleaned_data["id"]
                e = Employee.objects.get(id=id_)
                e.delete()
            else:
                print(form.errors.as_data())
            # Redirects to Employee/read
            return HttpResponseRedirect("../read")
        except ObjectDoesNotExist:
            return HttpResponseRedirect("../")
    else:
        form = EmployeeDeleteForm()
        return render(response, "main/emp_delete.html", {"form": form})


def games(response):
    game = Games.objects  # Get all Games
    data = []
    for g in game.all():
        data.append(g)
    return render(response, "main/games.html", {"games": game, "data": data})  # Render page and pass customers


def cus_view(response):
    return render(response, "main/cus_view.html", {})


def cus_buy(response):
    if response.method == "POST":
        form = CusBuyForm(response.POST)
        g_id = response.POST.get('Games')
        g = Games.objects.get(id=g_id)
        g.g_qty_sold += 1
        username_ = response.user.username
        user_id = Customer.objects.get(username=username_)
        t = Transaction(c_id=user_id, g_id=g)
        print(t)
        t.save()
        g.save()

        # Redirects to cus
        return HttpResponseRedirect("../")
    else:
        form = CusBuyForm()
    return render(response, "main/cus_buy.html", {"form": form})


def cus_order(response):
    t = Transaction.objects  # Get all Transactions
    data = []
    for e in t.all():
        if e.c_id.username == response.user.username:
            data.append(e)
    return render(response, "main/cus_order.html", {"t": t, "data": data})  # Render page and pass customers


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            username_ = response.POST.get('username')
            password = response.POST.get('password1')
            f_name = response.POST.get('f_name')
            l_name = response.POST.get('l_name')
            age = response.POST.get('age')
            c = Customer(f_name=f_name, l_name=l_name, username=username_, password=password, age=age)
            c.save()
            form.save()
            return redirect("../login/")

    form = RegisterForm()

    return render(response, "main/register.html", {"form": form})


def login(response):
    return redirect("../login/")
