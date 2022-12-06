from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Customer
from .forms import CustomerCreateForm, CustomerEditForm, CustomerDeleteForm
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
            c = Customer(f_name=f_name, l_name=l_name, age=age)
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
